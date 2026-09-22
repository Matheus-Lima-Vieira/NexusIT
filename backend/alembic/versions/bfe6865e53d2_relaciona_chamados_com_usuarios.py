"""relaciona chamados com usuarios

Revision ID: bfe6865e53d2
Revises: 27fd45bd772b
Create Date: 2026-09-22 17:25:39.166755

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfe6865e53d2'
down_revision: Union[str, Sequence[str], None] = '27fd45bd772b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("chamados", sa.Column("solicitante_id", sa.Integer(), nullable=True))

    op.execute("""
        UPDATE chamados
        SET solicitante_id = (
            SELECT id
            FROM usuarios
            WHERE perfil = 'Administrador'
            LIMIT 1
        )
        WHERE solicitante_id IS NULL
    """)

    op.alter_column("chamados", "solicitante_id", nullable=False)

    op.create_foreign_key(
        "fk_chamados_solicitante_id", "chamados", "usuarios", ["solicitante_id"], ["id"]
    )

    op.drop_column("chamados", "solicitante")


def downgrade() -> None:
    op.add_column(
        "chamados", sa.Column("solicitante", sa.VARCHAR(length=100), nullable=True)
    )

    op.execute("""
        UPDATE chamados c
        SET solicitante = u.nome
        FROM usuarios u
        WHERE c.solicitante_id = u.id
    """)

    op.alter_column("chamados", "solicitante", nullable=False)

    op.drop_constraint("fk_chamados_solicitante_id", "chamados", type_="foreignkey")

    op.drop_column("chamados", "solicitante_id")
