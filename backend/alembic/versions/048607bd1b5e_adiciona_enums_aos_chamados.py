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
        "Aberto", "Em andamento", "Resolvido", "Fechado", name="statuschamado"
    )

    prioridade_enum = postgresql.ENUM(
        "P1 - Muito alta",
        "P2 - Alta",
        "P3 - Média",
        "P4 - Baixa",
        "P5 - Muito baixa",
        name="prioridadechamado",
    )

    status_enum.create(op.get_bind())
    prioridade_enum.create(op.get_bind())

    op.alter_column(
        "chamados",
        "status",
        existing_type=sa.VARCHAR(length=30),
        type_=status_enum,
        existing_nullable=False,
        postgresql_using="status::statuschamado",
    )

    op.alter_column(
        "chamados",
        "prioridade",
        existing_type=sa.VARCHAR(length=20),
        type_=prioridade_enum,
        existing_nullable=False,
        postgresql_using="prioridade::prioridadechamado",
    )


def downgrade() -> None:
    status_enum = postgresql.ENUM(
        "Aberto", "Em andamento", "Resolvido", "Fechado", name="statuschamado"
    )

    prioridade_enum = postgresql.ENUM(
        "P1 - Muito alta",
        "P2 - Alta",
        "P3 - Média",
        "P4 - Baixa",
        "P5 - Muito baixa",
        name="prioridadechamado",
    )

    op.alter_column(
        "chamados",
        "prioridade",
        existing_type=prioridade_enum,
        type_=sa.VARCHAR(length=20),
        existing_nullable=False,
        postgresql_using="prioridade::text",
    )

    op.alter_column(
        "chamados",
        "status",
        existing_type=status_enum,
        type_=sa.VARCHAR(length=30),
        existing_nullable=False,
        postgresql_using="status::text",
    )

    prioridade_enum.drop(op.get_bind())
    status_enum.drop(op.get_bind())
