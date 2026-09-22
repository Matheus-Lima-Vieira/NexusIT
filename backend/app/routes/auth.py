from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from app.models.usuario import Usuario
from app.schemas.auth import LoginRequest, TokenResponse
from app.core.security import verificar_senha, criar_token_acesso
from app.core.dependencies import get_usuario_atual


router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/login", response_model=TokenResponse)
def login(dados: LoginRequest, db: Session = Depends(get_db)):

    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if usuario is None or not verificar_senha(dados.senha, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="E-mail ou senha inválidos.")

    token = criar_token_acesso(
        {
            "sub": str(usuario.id),
            "perfil": usuario.perfil.value,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }

@router.get("/me")
def usuario_atual(usuario: Usuario = Depends(get_usuario_atual)):
    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "perfil": usuario.perfil,
    }