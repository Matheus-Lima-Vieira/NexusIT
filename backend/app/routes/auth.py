from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from app.models.usuario import Usuario
from app.core.dependencies import get_usuario_atual
from app.schemas.usuarios import UsuarioResponse
from app.core.security import (
    verificar_senha,
    criar_token_acesso,
    criar_hash_senha,
)
from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
    AlterarSenhaRequest,
)


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

@router.get("/me", response_model=UsuarioResponse)
def usuario_atual(usuario: Usuario = Depends(get_usuario_atual)):
    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "perfil": usuario.perfil,
    }

@router.put("/password")
def alterar_senha(
    dados: AlterarSenhaRequest,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_usuario_atual),
):
    if not verificar_senha(dados.senha_atual, usuario.senha_hash):
        raise HTTPException(
            status_code=401,
            detail="Senha atual incorreta.",
        )

    usuario.senha_hash = criar_hash_senha(dados.nova_senha)

    db.commit()

    return {"mensagem": "Senha alterada com sucesso."}