"""atualiza status dos chamados

Revision ID: f6031c71a88c
Revises: c5e551b91264
Create Date: 2026-09-18 17:13:34.392182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6031c71a88c'
down_revision: Union[str, Sequence[str], None] = 'c5e551b91264'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE statuschamado RENAME TO statuschamado_old")

    op.execute("""
        CREATE TYPE statuschamado AS ENUM (
            'Novo',
            'Aberto',
            'Em andamento',
            'Encerrado',
            'Cancelado'
        )
    """)

    op.execute("""
        ALTER TABLE chamados
        ALTER COLUMN status
        TYPE statuschamado
        USING status::text::statuschamado
    """)

    op.execute("DROP TYPE statuschamado_old")


def downgrade() -> None:
    pass
