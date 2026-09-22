from enum import Enum


class StatusChamado(str, Enum):
    NOVO = "Novo"
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em andamento"
    ENCERRADO = "Encerrado"
    CANCELADO = "Cancelado"


class PrioridadeChamado(str, Enum):
    MUITO_ALTA = "P1 - Muito alta"
    ALTA = "P2 - Alta"
    MEDIA = "P3 - Média"
    BAIXA = "P4 - Baixa"
    MUITO_BAIXA = "P5 - Muito baixa"


class TipoHistorico(str, Enum):
    ALTERACAO = "Alteração"
    ANOTACAO = "Anotação"


class VisibilidadeHistorico(str, Enum):
    PUBLICO = "Público"
    INTERNO = "Interno"