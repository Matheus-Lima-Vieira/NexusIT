from pydantic import BaseModel, ConfigDict


class ChamadoBase(BaseModel):
    titulo: str
    descricao: str
    status: str
    prioridade: str
    solicitante: str


class ChamadoCreate(ChamadoBase):
    pass


class ChamadoUpdate(ChamadoBase):
    pass


class ChamadoResponse(ChamadoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
