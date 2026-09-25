import { Component, signal } from '@angular/core';
import { Auth as AuthService } from '../../core/services/auth';
import { Usuario } from '../../shared/models/usuario';

@Component({
  selector: 'app-dashboard',
  imports: [],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css',
})
export class Dashboard {
  usuario = signal<Usuario | null>(null);

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    this.authService.obterUsuarioAtual().subscribe({
      next: (resposta) => {
        this.usuario.set(resposta);

        console.log('Usuário autenticado:', this.usuario);
        console.log('Nome no Dashboard:', this.usuario()?.nome);
      },
      error: (erro) => {
        console.error('Erro ao buscar usuário:', erro);
      },
    });
  }
}