import jwt

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database import get_db
from app.core.security import SECRET_KEY, ALGORITHM
from app.models.usuario import Usuario
from app.enums.chamados import PerfilUsuario

bearer_scheme = HTTPBearer()


def get_usuario_atual(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> Usuario:

    credenciais_invalidas = HTTPException(
        status_code=401,
        detail="Não foi possível validar as credenciais.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token = credentials.credentials

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        usuario_id = payload.get("sub")

        if usuario_id is None:
            raise credenciais_invalidas

        usuario_id = int(usuario_id)

    except (jwt.PyJWTError, ValueError, TypeError):
        raise credenciais_invalidas

    usuario = db.get(Usuario, usuario_id)

    if usuario is None:
        raise credenciais_invalidas

    return usuario

def exigir_perfil(*perfis: PerfilUsuario):
    def verificar_perfil(
        usuario: Usuario = Depends(get_usuario_atual),
    ) -> Usuario:

        if usuario.perfil not in perfis:
            raise HTTPException(
                status_code=403,
                detail="Você não possui permissão para realizar esta ação.",
            )

        return usuario

    return verificar_perfil

exigir_admin = exigir_perfil(PerfilUsuario.ADMIN)

exigir_tecnico_ou_admin = exigir_perfil(
    PerfilUsuario.TECNICO,
    PerfilUsuario.ADMIN
)
