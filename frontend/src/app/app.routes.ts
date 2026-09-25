import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth-guard';

export const routes: Routes = [
    {
        path: 'login',
        loadComponent: () =>
            import('./features/auth/auth').then((m) => m.Auth),
    },
    {
        path: 'dashboard',
        canActivate: [authGuard],
        loadComponent: () =>
            import('./features/dashboard/dashboard').then((m) => m.Dashboard),
    },
    {
        path: 'chamados',
        loadComponent: () =>
            import('./features/chamados/chamados').then((m) => m.Chamados),
    },
    {
        path: 'usuarios',
        loadComponent: () =>
            import('./features/usuarios/usuarios').then((m) => m.Usuarios),
    },
    {
        path: 'perfil',
        loadComponent: () =>
            import('./features/perfil/perfil').then((m) => m.Perfil),
    },
    {
        path: '',
        redirectTo: 'login',
        pathMatch: 'full',
    },
    {
        path: '**',
        redirectTo: 'login',
    },
];