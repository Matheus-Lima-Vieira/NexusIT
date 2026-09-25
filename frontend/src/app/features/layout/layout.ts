import { Component } from '@angular/core';
import { Router, RouterLink, RouterOutlet } from '@angular/router';
import { Auth as AuthService } from '../../core/services/auth';

@Component({
  selector: 'app-layout',
  imports: [RouterLink, RouterOutlet],
  templateUrl: './layout.html',
  styleUrl: './layout.css',
})
export class Layout {
  constructor(
    private authService: AuthService,
    private router: Router,
  ) { }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }
}