export type TipoHistorico =
    | 'Alteração'
    | 'Anotação';

export type VisibilidadeHistorico =
    | 'Público'
    | 'Interno';

export interface Historico {
    id: number;
    chamado_id: number;
    autor_id: number;
    tipo: TipoHistorico;
    visibilidade: VisibilidadeHistorico;
    descricao: string;
    criado_em: string;
}