from getpass import getpass

from database import SessionLocal
from app.enums.chamados import PerfilUsuario
from app.schemas.usuarios import UsuarioCreate
from app.services.usuarios import criar_usuario
from app.models.usuario import Usuario


def criar_primeiro_admin():
    db = SessionLocal()

    try:
        admin_existente = (
            db.query(Usuario).filter(Usuario.perfil == PerfilUsuario.ADMIN).first()
        )

        if admin_existente:
            print("Já existe um administrador cadastrado.")
            return

        nome = input("Nome do administrador: ").strip()
        email = input("E-mail do administrador: ").strip().lower()

        senha = getpass("Senha: ")
        confirmar_senha = getpass("Confirme a senha: ")

        if senha != confirmar_senha:
            print("As senhas não coincidem.")
            return

        dados = UsuarioCreate(
            nome=nome,
            email=email,
            senha=senha,
            perfil=PerfilUsuario.ADMIN,
        )

        criar_usuario(db, dados)

        print("Administrador criado com sucesso!")

    except ValueError as erro:
        print(f"Erro: {erro}")

    finally:
        db.close()


if __name__ == "__main__":
    criar_primeiro_admin()
