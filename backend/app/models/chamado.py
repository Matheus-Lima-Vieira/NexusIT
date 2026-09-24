from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from app.enums.chamados import StatusChamado, PrioridadeChamado


class Chamado(Base):
    __tablename__ = "chamados"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)
    status = Column(
        Enum(
            StatusChamado,
            values_callable=lambda enum: [item.value for item in enum]
        ),
        nullable=False
    )

    prioridade = Column(
        Enum(
            PrioridadeChamado,
            values_callable=lambda enum: [item.value for item in enum]
        ),
        nullable=False
    )
    solicitante_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False,
    )
    solicitante = relationship(
    "Usuario",
    back_populates="chamados"
    )

    historicos = relationship(
        "HistoricoChamado",
        back_populates="chamado",
        cascade="all, delete-orphan"
    )
