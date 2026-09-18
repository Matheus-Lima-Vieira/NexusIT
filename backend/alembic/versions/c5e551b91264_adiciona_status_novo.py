"""adiciona status novo

Revision ID: c5e551b91264
Revises: 048607bd1b5e
Create Date: 2026-09-18 16:55:06.513121

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'c5e551b91264'
down_revision: Union[str, Sequence[str], None] = '048607bd1b5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE statuschamado ADD VALUE 'Novo' BEFORE 'Aberto'")


def downgrade() -> None:
    pass
