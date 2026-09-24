"""adiciona autor ao historico

Revision ID: 2194129b67bd
Revises: bfe6865e53d2
Create Date: 2026-09-23 15:50:51.983224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2194129b67bd'
down_revision: Union[str, Sequence[str], None] = 'bfe6865e53d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "historicos_chamados",
        sa.Column("autor_id", sa.Integer(), nullable=True),
    )

    op.execute("UPDATE historicos_chamados SET autor_id = 1")

    op.alter_column(
        "historicos_chamados",
        "autor_id",
        existing_type=sa.Integer(),
        nullable=False,
    )

    op.create_foreign_key(
        "fk_historicos_chamados_autor_id",
        "historicos_chamados",
        "usuarios",
        ["autor_id"],
        ["id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_historicos_chamados_autor_id",
        "historicos_chamados",
        type_="foreignkey",
    )

    op.drop_column(
        "historicos_chamados",
        "autor_id",
    )
