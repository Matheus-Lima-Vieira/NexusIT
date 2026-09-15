from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Chamado as ChamadoModel

from app.routes.chamados import router as chamados_router
from app.schemas.chamados import Chamado

app = FastAPI()
app.include_router(chamados_router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Nexus IT API"}
