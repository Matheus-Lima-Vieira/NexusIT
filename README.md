# Nexus IT

Sistema de Gestão de Serviços de TI.

Projeto Full Stack desenvolvido para estudo e portfólio.

## Tecnologias

* Angular
* TypeScript
* Python
* FastAPI
* PostgreSQL
* SQLAlchemy

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

### 4. Inicie o servidor

```powershell
uvicorn main:app --reload
```

A API estará disponível em:

`http://127.0.0.1:8000`

A documentação interativa da API (Swagger) estará disponível em:

`http://127.0.0.1:8000/docs`
