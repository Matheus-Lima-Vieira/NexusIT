import { Injectable } from '@angular/core';
import { Api } from './api';
import { Chamado } from '../../shared/models/chamado';

@Injectable({
    providedIn: 'root',
})
export class Chamados {
    constructor(private api: Api) { }

    listar() {
        return this.api.get<Chamado[]>('/chamados/');
    }
}