from sqlalchemy import Column, Integer, Text, ForeignKey, Enum, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base
from app.enums.chamados import TipoHistorico, VisibilidadeHistorico


class HistoricoChamado(Base):
    __tablename__ = "historicos_chamados"

    id = Column(Integer, primary_key=True)

    chamado_id = Column(Integer, ForeignKey("chamados.id"), nullable=False)

    tipo = Column(
        Enum(TipoHistorico, values_callable=lambda enum: [item.value for item in enum]),
        nullable=False,
    )

    visibilidade = Column(
        Enum(
            VisibilidadeHistorico,
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=False,
    )

    descricao = Column(Text, nullable=False)

    criado_em = Column(DateTime, server_default=func.now(), nullable=False)

    chamado = relationship("Chamado", back_populates="historicos")
