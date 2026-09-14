from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Chamado as ChamadoModel

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Nexus IT API"}

class Chamado(BaseModel):
    titulo: str
    descricao: str
    status: str
    prioridade: str
    solicitante: str

@app.post("/chamados/")
def criar_chamado(chamado: Chamado, db: Session = Depends(get_db)):
    novo_chamado = ChamadoModel(
    titulo=chamado.titulo,
    descricao=chamado.descricao,
    status=chamado.status,
    prioridade=chamado.prioridade,
    solicitante=chamado.solicitante
)

    db.add(novo_chamado)
    db.commit()
    db.refresh(novo_chamado)

    return novo_chamado

@app.get("/chamados/")
def receber_chamados(db: Session = Depends(get_db)):
    chamados = db.query(ChamadoModel).all()

    return chamados

@app.get("/chamados/{id}")
def receber_chamado(id: int, db: Session = Depends(get_db)):
    chamado = db.get(ChamadoModel, id)

    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    return chamado
    
@app.put("/chamados/{id}")
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

@app.delete("/chamados/{id}")
def excluir_chamado(id: int, db: Session = Depends(get_db)):
    chamado = db.get(ChamadoModel, id)
    if chamado is None:
        raise HTTPException(status_code=404, detail="Chamado não encontrado!")

    db.delete(chamado)
    db.commit()

    return {"mensagem": "Removido com sucesso!"}
