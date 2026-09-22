from sqlalchemy.orm import Session

from app.core.security import criar_hash_senha
from app.models.usuario import Usuario
from app.schemas.usuarios import UsuarioCreate


def criar_usuario(db: Session, dados: UsuarioCreate) -> Usuario:
    email_existente = db.query(Usuario).filter(Usuario.email == dados.email).first()

    if email_existente:
        raise ValueError("E-mail já cadastrado.")

    novo_usuario = Usuario(
        nome=dados.nome,
        email=dados.email,
        senha_hash=criar_hash_senha(dados.senha),
        perfil=dados.perfil,
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario
