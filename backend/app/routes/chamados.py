from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from app.models.chamado import Chamado as ChamadoModel
from app.schemas.chamados import ChamadoCreate, ChamadoUpdate, ChamadoResponse

router = APIRouter()


@router.get("/chamados/", response_model=list[ChamadoResponse])
def receber_chamados(db: Session = Depends(get_db)):
    chamados = db.query(ChamadoModel).all()

    return chamados

@router.post("/chamados/", response_model=ChamadoResponse)
def criar_chamado(chamado: ChamadoCreate, db: Session = Depends(get_db)):
    novo_chamado = ChamadoModel(
        titulo=chamado.titulo,
        descricao=chamado.descricao,
        status=chamado.status,
        prioridade=chamado.prioridade,
        solicitante=chamado.solicitante,
    )

    db.add(novo_chamado)
    db.commit()
    db.refresh(novo_chamado)

    return novo_chamado

@router.get("/chamados/{id}", response_model=ChamadoResponse)
def receber_chamado(id: int, db: Session = Depends(get_db)):
    chamado = db.get(ChamadoModel, id)

    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    return chamado

@router.put("/chamados/{id}", response_model=ChamadoResponse)
def alterar_chamado(id: int, dados: ChamadoUpdate, db: Session = Depends(get_db)):
    chamado = db.get(ChamadoModel, id)

    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    dados_atualizacao = dados.model_dump(exclude_unset=True)

    for campo, valor in dados_atualizacao.items():
        setattr(chamado, campo, valor)

    db.commit()
    db.refresh(chamado)

    return chamado


@router.delete("/chamados/{id}")
def excluir_chamado(id: int, db: Session = Depends(get_db)):
    chamado = db.get(ChamadoModel, id)
    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    db.delete(chamado)
    db.commit()

    return {"mensagem": "Removido com sucesso!"}
