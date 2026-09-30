import { Injectable } from '@angular/core';
import { Api } from './api';
import { Chamado } from '../../shared/models/chamado';
import { ChamadoUpdate } from '../../shared/models/chamado-update';
import {
    Historico,
    VisibilidadeHistorico,
} from '../../shared/models/historico';

@Injectable({
    providedIn: 'root',
})
export class Chamados {
    constructor(private api: Api) { }

    listar() {
        return this.api.get<Chamado[]>('/chamados/');
    }

    obterPorId(id: number) {
        return this.api.get<Chamado>(`/chamados/${id}`);
    }

    listarHistorico(chamadoId: number) {
        return this.api.get<Historico[]>(
            `/chamados/${chamadoId}/historico`,
        );
    }

    criarAnotacao(
        chamadoId: number,
        descricao: string,
        visibilidade: VisibilidadeHistorico,
    ) {
        return this.api.post<Historico>(
            `/chamados/${chamadoId}/historico`,
            {
                descricao,
                visibilidade,
            },
        );
    }

    alterar(id: number, dados: ChamadoUpdate) {
        return this.api.put<Chamado>(
            `/chamados/${id}`,
            dados,
        );
    }
}