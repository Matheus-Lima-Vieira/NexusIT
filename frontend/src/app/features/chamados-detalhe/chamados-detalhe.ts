import { Component, OnInit, signal } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Chamados } from '../../core/services/chamados';
import { Chamado } from '../../shared/models/chamado';
import {Historico, VisibilidadeHistorico,} from '../../shared/models/historico';
import { FormsModule } from '@angular/forms';
import { Auth } from '../../core/services/auth';
import { Usuario } from '../../shared/models/usuario';
import {
  STATUS_CHAMADO,
  PRIORIDADE_CHAMADO,
} from '../../shared/constants/chamado-options';

@Component({
  selector: 'app-chamados-detalhe',
  imports: [FormsModule],
  templateUrl: './chamados-detalhe.html',
  styleUrl: './chamados-detalhe.css',
})
export class ChamadosDetalhe implements OnInit {
  chamado = signal<Chamado | null>(null);
  historico = signal<Historico[]>([]);
  novaAnotacao = '';
  visibilidadeAnotacao: 'Público' | 'Interno' = 'Público';
  usuarioAtual = signal<Usuario | null>(null);
  statusSelecionado = '';
  prioridadeSelecionada = '';
  statusOptions = STATUS_CHAMADO;
  prioridadeOptions = PRIORIDADE_CHAMADO;

  constructor(
    private route: ActivatedRoute,
    private chamadosService: Chamados,
    private authService: Auth,
  ) { }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));

    this.authService.obterUsuarioAtual().subscribe({
      next: (resposta) => {
        this.usuarioAtual.set(resposta);
      },
      error: (erro) => {
        console.error('Erro ao buscar usuário atual:', erro);
      },
    });
    
    this.chamadosService.obterPorId(id).subscribe({
      next: (resposta) => {
        this.chamado.set(resposta);

        this.statusSelecionado = resposta.status;
        this.prioridadeSelecionada = resposta.prioridade;

        console.log('Chamado carregado:', resposta);
      },
    });

    this.chamadosService.listarHistorico(id).subscribe({
      next: (resposta) => {
        this.historico.set(resposta);
        console.log('Histórico carregado:', resposta);
      },
      error: (erro) => {
        console.error('Erro ao buscar histórico:', erro);
      },
    });
  }
  adicionarAnotacao(): void {
    const chamadoAtual = this.chamado();

    if (!chamadoAtual || !this.novaAnotacao.trim()) {
      return;
    }

    this.chamadosService.criarAnotacao(
      chamadoAtual.id,
      this.novaAnotacao.trim(),
      this.visibilidadeAnotacao,
    ).subscribe({
      next: (resposta) => {
        console.log('Anotação criada:', resposta);

        this.historico.update((historicos) => [
          ...historicos,
          resposta,
        ]);

        this.novaAnotacao = '';
      },
      error: (erro) => {
        console.error('Erro ao criar anotação:', erro);
      },
    });
  }

  podeEditarChamado(): boolean {
    const perfil = this.usuarioAtual()?.perfil;

    return perfil === 'Técnico' || perfil === 'Administrador';
  }
  
  temAlteracao(): boolean {
    const chamadoAtual = this.chamado();

    if (!chamadoAtual) {
      return false;
    }

    return (
      this.statusSelecionado !== chamadoAtual.status ||
      this.prioridadeSelecionada !== chamadoAtual.prioridade
    );
  }
}