from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_serializer

from app.enums.chamados import (
    StatusChamado,
    PrioridadeChamado,
    TipoHistorico,
    VisibilidadeHistorico,
)

class ChamadoBase(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    descricao: str = Field(min_length=5)
    status: StatusChamado = StatusChamado.NOVO
    prioridade: PrioridadeChamado = PrioridadeChamado.MEDIA
    solicitante: str = Field(min_length=3, max_length=100)


class ChamadoCreate(ChamadoBase):
    pass


class ChamadoUpdate(BaseModel):
    titulo: str | None = Field(default=None, min_length=3, max_length=100)
    descricao: str | None = Field(default=None, min_length=5)
    status: StatusChamado | None = None
    prioridade: PrioridadeChamado | None = None
    solicitante: str | None = Field(default=None, min_length=3, max_length=100)


class ChamadoResponse(ChamadoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class HistoricoResponse(BaseModel):
    id: int
    chamado_id: int
    tipo: TipoHistorico
    visibilidade: VisibilidadeHistorico
    descricao: str
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("criado_em")
    def formatar_data(self, valor: datetime) -> str:
        return valor.strftime("%Y-%m-%d - %H:%M:%S")

class HistoricoCreate(BaseModel):
    descricao: str = Field(min_length=1)
    visibilidade: VisibilidadeHistorico = VisibilidadeHistorico.PUBLICO