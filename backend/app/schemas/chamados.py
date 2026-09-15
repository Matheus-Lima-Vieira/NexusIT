from pydantic import BaseModel


class Chamado(BaseModel):
    titulo: str
    descricao: str
    status: str
    prioridade: str
    solicitante: str
