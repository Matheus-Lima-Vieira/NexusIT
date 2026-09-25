import { Component, OnInit, signal } from '@angular/core';
import { Chamados as ChamadosService } from '../../core/services/chamados';
import { Chamado } from '../../shared/models/chamado';

@Component({
  selector: 'app-chamados',
  imports: [],
  templateUrl: './chamados.html',
  styleUrl: './chamados.css',
})
export class Chamados implements OnInit {
  chamados = signal<Chamado[]>([]);

  constructor(private chamadosService: ChamadosService) { }

  ngOnInit(): void {
    this.chamadosService.listar().subscribe({
      next: (resposta) => {
        this.chamados.set(resposta);
        console.log('Chamados:', resposta);
      },
      error: (erro) => {
        console.error('Erro ao buscar chamados:', erro);
      },
    });
  }
}