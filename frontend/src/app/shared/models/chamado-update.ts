import {
    PrioridadeChamado,
    StatusChamado,
} from './chamado';

export interface ChamadoUpdate {
    titulo?: string;
    descricao?: string;
    status?: StatusChamado;
    prioridade?: PrioridadeChamado;
}