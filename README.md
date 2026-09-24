# Nexus IT

Sistema de Gestão de Serviços de TI.

Projeto Full Stack desenvolvido para estudo, prática e portfólio, simulando uma aplicação interna de gerenciamento de chamados de suporte técnico.

## Tecnologias

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* Pydantic
* JWT
* pwdlib / Argon2

### Frontend

* Angular
* TypeScript
* HTML
* CSS
* RxJS

> O frontend está em desenvolvimento. Atualmente, o backend concentra a implementação principal do sistema.

## Funcionalidades atuais

* Autenticação de usuários com JWT
* Controle de acesso por perfil:

  * Solicitante
  * Técnico
  * Administrador
* Criação e consulta de chamados
* Atualização de chamados por usuários autorizados
* Exclusão de chamados restrita a administradores
* Controle de status e prioridade
* Histórico de alterações dos chamados
* Anotações públicas e internas
* Controle de visibilidade das anotações
* Identificação do autor das alterações e anotações
* Criação de usuários por administradores
* Alteração de senha pelo próprio usuário
* Documentação da API com Swagger/OpenAPI
* Migrations do banco de dados com Alembic

## Estrutura do projeto

```text
NexusIT/
├── backend/
│   ├── alembic/
│   ├── app/
│   │   ├── core/
│   │   ├── enums/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── services/
│   ├── scripts/
│   ├── .env
│   ├── alembic.ini
│   ├── database.py
│   ├── main.py
│   └── requirements.txt
├── docs/
├── frontend/
├── .gitignore
└── README.md
```

## Como executar a API

### 1. Acesse a pasta do backend

Na raiz do projeto:

```powershell
cd backend
```

### 2. Ative o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` dentro da pasta `backend`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/nexus_it
SECRET_KEY=sua_chave_secreta
```

> O arquivo `.env` não deve ser versionado. Ele já está incluído no `.gitignore`.

### 5. Execute as migrations

```powershell
alembic upgrade head
```

### 6. Inicie o servidor

```powershell
uvicorn main:app --reload
```

A API estará disponível em:

`http://127.0.0.1:8000`

### Documentação da API

Swagger:

`http://127.0.0.1:8000/docs`

ReDoc:

`http://127.0.0.1:8000/redoc`

## Banco de dados

O projeto utiliza PostgreSQL como banco de dados e SQLAlchemy como ORM.

As alterações estruturais do banco são controladas pelo Alembic.

Para verificar a versão atual das migrations:

```powershell
alembic current
```

Para verificar se existem alterações nos models que ainda não foram transformadas em migration:

```powershell
alembic check
```

## Autenticação

A API utiliza autenticação baseada em JWT.

O acesso aos endpoints protegidos requer um token obtido através de:

```text
POST /auth/login
```

O token deve ser enviado nas requisições autenticadas utilizando o esquema:

```text
Authorization: Bearer <token>
```

## Perfis de usuário

O sistema possui três perfis:

| Perfil        | Descrição                                    |
| ------------- | -------------------------------------------- |
| Solicitante   | Abre e acompanha seus próprios chamados      |
| Técnico       | Gerencia os chamados de suporte              |
| Administrador | Possui permissões administrativas adicionais |

O controle de acesso é realizado no backend através de dependências de autenticação e autorização.

## Objetivo do projeto

O Nexus IT está sendo desenvolvido como projeto de estudo e portfólio para praticar conceitos de desenvolvimento Full Stack, incluindo:

* Desenvolvimento de APIs REST
* Autenticação e autorização
* Modelagem de banco de dados
* ORM
* Migrations
* Validação de dados
* Controle de acesso
* Arquitetura de aplicações
* Integração entre frontend e backend
* Git e GitHub

## Status do projeto

**Backend:** em desenvolvimento

**Frontend:** em desenvolvimento
