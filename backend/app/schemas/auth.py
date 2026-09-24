from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr
    senha: str = Field(min_length=8, max_length=100)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class AlterarSenhaRequest(BaseModel):
    senha_atual: str = Field(min_length=8, max_length=100)
    nova_senha: str = Field(min_length=8, max_length=100)
