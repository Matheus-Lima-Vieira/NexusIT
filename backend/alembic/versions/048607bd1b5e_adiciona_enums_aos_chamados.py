"""adiciona enums aos chamados

Revision ID: 048607bd1b5e
Revises: 
Create Date: 2026-09-18 16:42:34.292077

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '048607bd1b5e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    status_enum = postgresql.ENUM(
        "Aberto",
        "Em andamento",
        "Resolvido",
        "Fechado",
        name="statuschamado",
    )

    prioridade_enum = postgresql.ENUM(
        "P1 - Muito alta",
        "P2 - Alta",
        "P3 - Média",
        "P4 - Baixa",
        "P5 - Muito baixa",
        name="prioridadechamado",
    )

    op.create_table(
        "chamados",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("titulo", sa.String(length=100), nullable=False),
        sa.Column("descricao", sa.Text(), nullable=False),
        sa.Column("status", status_enum, nullable=False),
        sa.Column("prioridade", prioridade_enum, nullable=False),
        sa.Column("solicitante", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("chamados")

    prioridade_enum = postgresql.ENUM(
        "P1 - Muito alta",
        "P2 - Alta",
        "P3 - Média",
        "P4 - Baixa",
        "P5 - Muito baixa",
        name="prioridadechamado",
    )

    status_enum = postgresql.ENUM(
        "Aberto",
        "Em andamento",
        "Resolvido",
        "Fechado",
        name="statuschamado",
    )

    prioridade_enum.drop(op.get_bind())
    status_enum.drop(op.get_bind())