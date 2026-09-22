from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from database import Base
from app.enums.chamados import PerfilUsuario


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)

    perfil = Column(
        Enum(PerfilUsuario, values_callable=lambda enum: [item.value for item in enum]),
        nullable=False,
    )

    chamados = relationship("Chamado", back_populates="solicitante")
