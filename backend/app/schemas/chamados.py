from pydantic import BaseModel, ConfigDict
from app.enums.chamados import StatusChamado, PrioridadeChamado

class ChamadoBase(BaseModel):
    titulo: str
    descricao: str
    status: StatusChamado = StatusChamado.NOVO
    prioridade: PrioridadeChamado = PrioridadeChamado.MEDIA
    solicitante: str


class ChamadoCreate(ChamadoBase):
    pass


class ChamadoUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    status: StatusChamado | None = None
    prioridade: PrioridadeChamado | None = None
    solicitante: str | None = None


class ChamadoResponse(ChamadoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
