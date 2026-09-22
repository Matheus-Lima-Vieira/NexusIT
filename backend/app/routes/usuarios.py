from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from app.core.dependencies import exigir_perfil
from app.enums.chamados import PerfilUsuario
from app.models.usuario import Usuario
from app.schemas.usuarios import UsuarioCreate, UsuarioResponse
from app.services.usuarios import criar_usuario

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post(
    "/",
    response_model=UsuarioResponse,
)
def criar_novo_usuario(
    dados: UsuarioCreate,
    db: Session = Depends(get_db),
    usuario_atual: Usuario = Depends(exigir_perfil(PerfilUsuario.ADMIN)),
):
    try:
        return criar_usuario(db, dados)

    except ValueError as erro:
        raise HTTPException(
            status_code=400,
            detail=str(erro),
        )
