from sqlalchemy import Column, Integer, String, Text

from database import Base


class Chamado(Base):
    __tablename__ = "chamados"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)
    status = Column(String(30), nullable=False)
    prioridade = Column(String(20), nullable=False)
    solicitante = Column(String(100), nullable=False)
