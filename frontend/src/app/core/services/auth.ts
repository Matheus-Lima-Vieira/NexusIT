import { Injectable } from '@angular/core';
import { Api } from './api';
import { Usuario } from '../../shared/models/usuario';

interface LoginRequest {
  email: string;
  senha: string;
}

interface TokenResponse {
  access_token: string;
  token_type: string;
}

@Injectable({
  providedIn: 'root',
})

export class Auth {
  constructor(private api: Api) { }

  login(email: string, senha: string) {
    const dados: LoginRequest = {
      email,
      senha,
    };

    return this.api.post<TokenResponse>('/auth/login', dados);
  }

  obterUsuarioAtual() {
    return this.api.get<Usuario>('/auth/me');
  }

  salvarToken(token: string): void {
    localStorage.setItem('access_token', token);
  }

  obterToken(): string | null {
    return localStorage.getItem('access_token');
  }

  removerToken(): void {
    localStorage.removeItem('access_token');
  }

  logout(): void {
    this.removerToken();
  }
}