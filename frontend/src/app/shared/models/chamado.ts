export type StatusChamado =
    | 'Novo'
    | 'Pendente'
    | 'Em andamento'
    | 'Encerrado'
    | 'Cancelado';

export type PrioridadeChamado =
    | 'P1 - Muito alta'
    | 'P2 - Alta'
    | 'P3 - Média'
    | 'P4 - Baixa'
    | 'P5 - Muito baixa';

export interface Chamado {
    id: number;
    titulo: string;
    descricao: string;
    status: StatusChamado;
    prioridade: PrioridadeChamado;
    solicitante_id: number;
}