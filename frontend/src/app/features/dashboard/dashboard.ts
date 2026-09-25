import { Component, signal } from '@angular/core';
import { Router } from '@angular/router';
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

  constructor(
    private authService: AuthService,
    private router: Router,
  ) { }

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

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }
}