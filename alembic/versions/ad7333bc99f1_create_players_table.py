"""create players table

Revision ID: ad7333bc99f1
Revises: 
Create Date: 2022-08-28 15:13:58.926600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad7333bc99f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'players',
        sa.Column('tag', sa.String(20), primary_key=True, nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('role', sa.String(10), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('players')
