from sqlalchemy import Column, Integer, String, Text, Enum

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
    solicitante = Column(String(100), nullable=False)
