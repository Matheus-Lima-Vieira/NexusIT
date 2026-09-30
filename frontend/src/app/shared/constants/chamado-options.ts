import { PrioridadeChamado, StatusChamado } from '../models/chamado';

export const STATUS_CHAMADO: StatusChamado[] = [
    'Novo',
    'Pendente',
    'Em andamento',
    'Encerrado',
    'Cancelado',
];

export const PRIORIDADE_CHAMADO: PrioridadeChamado[] = [
    'P1 - Muito alta',
    'P2 - Alta',
    'P3 - Média',
    'P4 - Baixa',
    'P5 - Muito baixa',
];