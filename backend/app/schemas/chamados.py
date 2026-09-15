from pydantic import BaseModel, ConfigDict
from enum import Enum

class StatusChamado(str, Enum):
    ABERTO = "Aberto"
    EM_ANDAMENTO = "Em andamento"
    RESOLVIDO = "Resolvido"
    FECHADO = "Fechado"

class PrioridadeChamado(str, Enum):
    MUITO_ALTA = "P1 - Muito alta"
    ALTA = "P2 - Alta"
    MEDIA = "P3 - Média"
    BAIXA = "P4 - Baixa"
    MUITO_BAIXA = "P5 - Muito baixa"

class ChamadoBase(BaseModel):
    titulo: str
    descricao: str
    status: StatusChamado
    prioridade: PrioridadeChamado = PrioridadeChamado.MEDIA
    solicitante: str


class ChamadoCreate(ChamadoBase):
    pass


class ChamadoUpdate(ChamadoBase):
    pass


class ChamadoResponse(ChamadoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
