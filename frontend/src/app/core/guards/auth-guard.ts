import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { Auth as AuthService } from '../services/auth';

export const authGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);

  const token = authService.obterToken();

  if (token) {
    return true;
  }

  return router.createUrlTree(['/login']);
};