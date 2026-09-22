from pydantic import BaseModel, ConfigDict, Field

from app.enums.chamados import StatusChamado, PrioridadeChamado


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
