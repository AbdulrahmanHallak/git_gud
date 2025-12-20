"""initial schema

Revision ID: e7c87166e871
Revises: 630f0df4c720
Create Date: 2025-12-20 22:08:36.199609

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7c87166e871'
down_revision: Union[str, Sequence[str], None] = '630f0df4c720'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
