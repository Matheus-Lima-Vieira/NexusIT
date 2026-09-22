from pydantic import BaseModel, ConfigDict, Field

from app.enums.chamados import PerfilUsuario


class UsuarioCreate(BaseModel):
    nome: str = Field(min_length=3, max_length=100)
    email: str = Field(min_length=5, max_length=150)
    senha: str = Field(min_length=8, max_length=100)
    perfil: PerfilUsuario


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    perfil: PerfilUsuario

    model_config = ConfigDict(from_attributes=True)
