import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Auth as AuthService } from '../../core/services/auth';

@Component({
  selector: 'app-auth',
  imports: [FormsModule],
  templateUrl: './auth.html',
  styleUrl: './auth.css',
})
export class Auth {
  email = '';
  senha = '';

  constructor(
    private authService: AuthService,
    private router: Router,
  ) { }

  login(): void {
    console.log('Botão Entrar clicado');
    console.log('E-mail:', this.email);
    console.log('Senha:', this.senha);

    this.authService.login(this.email, this.senha).subscribe({
      next: (resposta) => {
        this.authService.salvarToken(resposta.access_token);
        this.router.navigate(['/dashboard']);

        console.log('Login realizado:', resposta);
        console.log('Token salvo:', this.authService.obterToken());
      },
      error: (erro) => {
        console.error('Erro no login:', erro);
      },
    });
  }
}