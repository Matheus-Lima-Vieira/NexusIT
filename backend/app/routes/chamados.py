from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from app.models.chamado import Chamado as ChamadoModel
from app.schemas.chamados import Chamado


router = APIRouter()


@router.get("/chamados/")
def receber_chamados(db: Session = Depends(get_db)):
    chamados = db.query(ChamadoModel).all()

    return chamados

@router.post("/chamados/")
def criar_chamado(chamado: Chamado, db: Session = Depends(get_db)):
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

@router.get("/chamados/{id}")
def receber_chamado(id: int, db: Session = Depends(get_db)):
    chamado = db.get(ChamadoModel, id)

    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    return chamado

@router.put("/chamados/{id}")
def alterar_chamado(id: int, dados: Chamado, db: Session = Depends(get_db)):
    chamado = db.get(ChamadoModel, id)
    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")
    chamado.titulo = dados.titulo
    chamado.descricao = dados.descricao
    chamado.status = dados.status
    chamado.prioridade = dados.prioridade
    chamado.solicitante = dados.solicitante

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