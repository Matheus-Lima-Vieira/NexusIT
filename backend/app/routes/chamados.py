from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from app.models.chamado import Chamado as ChamadoModel
from app.models.historico import HistoricoChamado
from app.core.dependencies import (
    get_usuario_atual,
    exigir_tecnico_ou_admin,
    exigir_admin,
)
from app.models.usuario import Usuario
from app.schemas.chamados import (
    ChamadoCreate,
    ChamadoUpdate,
    ChamadoResponse,
    HistoricoResponse,
    HistoricoCreate
)
from app.enums.chamados import (
    StatusChamado,
    TipoHistorico,
    VisibilidadeHistorico,
    PerfilUsuario,
)

router = APIRouter()

TRANSICOES_PERMITIDAS = {
    StatusChamado.NOVO: {
        StatusChamado.PENDENTE,
        StatusChamado.EM_ANDAMENTO,
        StatusChamado.ENCERRADO,
        StatusChamado.CANCELADO,
    },
    StatusChamado.PENDENTE: {
        StatusChamado.NOVO,
        StatusChamado.EM_ANDAMENTO,
        StatusChamado.ENCERRADO,
        StatusChamado.CANCELADO,
    },
    StatusChamado.EM_ANDAMENTO: {
        StatusChamado.PENDENTE,
        StatusChamado.ENCERRADO,
        StatusChamado.CANCELADO,
    },
    StatusChamado.ENCERRADO: {
        StatusChamado.EM_ANDAMENTO,
    },
    StatusChamado.CANCELADO: set(),
}

NOMES_CAMPOS = {
    "titulo": "Título alterado",
    "descricao": "Descrição alterada",
    "status": "Status alterado",
    "prioridade": "Prioridade alterada",
}

@router.get("/chamados/", response_model=list[ChamadoResponse])
def receber_chamados(
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(get_usuario_atual),
):
    if usuario_atual.perfil in {
        PerfilUsuario.TECNICO,
        PerfilUsuario.ADMIN,
    }:
        chamados = db.query(ChamadoModel).all()
    else:
        chamados = (
            db.query(ChamadoModel)
            .filter(ChamadoModel.solicitante_id == usuario_atual.id)
            .all()
        )

    return chamados

@router.post("/chamados/", response_model=ChamadoResponse)
def criar_chamado(
    chamado: ChamadoCreate,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(get_usuario_atual),
):
    novo_chamado = ChamadoModel(
        titulo=chamado.titulo,
        descricao=chamado.descricao,
        status=chamado.status,
        prioridade=chamado.prioridade,
        solicitante_id=usuario_atual.id,
    )

    historico = HistoricoChamado(
        chamado=novo_chamado,
        autor_id=usuario_atual.id,
        tipo=TipoHistorico.ALTERACAO,
        visibilidade=VisibilidadeHistorico.PUBLICO,
        descricao="Chamado criado.",
    )

    db.add(novo_chamado)
    db.add(historico)
    db.commit()
    db.refresh(novo_chamado)

    return novo_chamado

@router.get("/chamados/{id}", response_model=ChamadoResponse)
def receber_chamado(
    id: int,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(get_usuario_atual),
    ):
    chamado = db.get(ChamadoModel, id)


    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    if (
        usuario_atual.perfil == PerfilUsuario.SOLICITANTE
        and chamado.solicitante_id != usuario_atual.id
    ):
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    return chamado

@router.put("/chamados/{id}", response_model=ChamadoResponse)
def alterar_chamado(
    id: int,
    dados: ChamadoUpdate,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(exigir_tecnico_ou_admin),
):
    chamado = db.get(ChamadoModel, id)

    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    if (
        dados.status is not None
        and dados.status not in TRANSICOES_PERMITIDAS[chamado.status]
    ):
        raise HTTPException(
            status_code=400, detail="Transição de status não permitida."
        )

    if dados.prioridade is not None and chamado.status in {
        StatusChamado.ENCERRADO,
        StatusChamado.CANCELADO,
    }:
        raise HTTPException(
            status_code=400,
            detail="Não é possível alterar a prioridade após encerramento ou cancelamento do chamado",
        )

    dados_atualizacao = dados.model_dump(exclude_unset=True)

    historicos = []

    for campo, novo_valor in dados_atualizacao.items():
        valor_anterior = getattr(chamado, campo)

        if valor_anterior != novo_valor:
            historicos.append(
                HistoricoChamado(
                    chamado=chamado,
                    autor_id=usuario_atual.id,
                    tipo=TipoHistorico.ALTERACAO,
                    visibilidade=VisibilidadeHistorico.PUBLICO,
                    descricao=(
                        f"{NOMES_CAMPOS[campo]}: "
                        f"{valor_anterior.value if hasattr(valor_anterior, 'value') else valor_anterior}"
                        f" → "
                        f"{novo_valor.value if hasattr(novo_valor, 'value') else novo_valor}"
                    ),
                )
            )

            setattr(chamado, campo, novo_valor)

    for historico in historicos:
        db.add(historico)

    db.commit()
    db.refresh(chamado)

    return chamado

@router.delete("/chamados/{id}")
def excluir_chamado(
    id: int,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(exigir_admin),
):
    chamado = db.get(ChamadoModel, id)
    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    db.delete(chamado)
    db.commit()

    return {"mensagem": "Removido com sucesso!"}

@router.get("/chamados/{id}/historico", response_model=list[HistoricoResponse])
def receber_historico(
    id: int,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(get_usuario_atual),
):
    chamado = db.get(ChamadoModel, id)

    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    if (
        usuario_atual.perfil == PerfilUsuario.SOLICITANTE
        and chamado.solicitante_id != usuario_atual.id
    ):
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    consulta = (
        db.query(HistoricoChamado)
        .filter(HistoricoChamado.chamado_id == id)
    )

    if usuario_atual.perfil == PerfilUsuario.SOLICITANTE:
        consulta = consulta.filter(
            HistoricoChamado.visibilidade == VisibilidadeHistorico.PUBLICO
        )

    historicos = (
        consulta
        .order_by(HistoricoChamado.criado_em)
        .all()
    )

    return historicos

@router.post("/chamados/{id}/historico", response_model=HistoricoResponse)
def criar_anotacao(
    id: int,
    historico: HistoricoCreate,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(get_usuario_atual),
):
    chamado = db.get(ChamadoModel, id)

    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    if (
        usuario_atual.perfil == PerfilUsuario.SOLICITANTE
        and chamado.solicitante_id != usuario_atual.id
    ):
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    if (
        usuario_atual.perfil == PerfilUsuario.SOLICITANTE
        and historico.visibilidade == VisibilidadeHistorico.INTERNO
    ):
        raise HTTPException(
            status_code=403,
            detail="Solicitantes não podem criar anotações internas.",
        )

    nova_anotacao = HistoricoChamado(
        chamado=chamado,
        autor_id=usuario_atual.id,
        tipo=TipoHistorico.ANOTACAO,
        visibilidade=historico.visibilidade,
        descricao=historico.descricao,
    )

    db.add(nova_anotacao)
    db.commit()
    db.refresh(nova_anotacao)

    return nova_anotacao
