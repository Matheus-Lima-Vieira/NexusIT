import os

import jwt
from pwdlib import PasswordHash
from dotenv import load_dotenv

from datetime import datetime, timedelta, timezone


load_dotenv()

password_hash = PasswordHash.recommended()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"


def criar_hash_senha(senha: str) -> str:
    return password_hash.hash(senha)


def verificar_senha(senha: str, senha_hash: str) -> bool:
    return password_hash.verify(senha, senha_hash)


def criar_token_acesso(dados: dict) -> str:
    dados_token = dados.copy()

    expiracao = datetime.now(timezone.utc) + timedelta(minutes=30)
    dados_token.update({"exp": expiracao})

    return jwt.encode(dados_token, SECRET_KEY, algorithm=ALGORITHM)