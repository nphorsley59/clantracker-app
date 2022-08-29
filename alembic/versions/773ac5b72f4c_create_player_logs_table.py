"""create player logs table

Revision ID: 773ac5b72f4c
Revises: ad7333bc99f1
Create Date: 2022-08-28 22:11:10.122758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '773ac5b72f4c'
down_revision = 'ad7333bc99f1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'player_logs',
        sa.Column('tag', sa.String(20), nullable=False),
        sa.Column('exp_level', sa.Integer, nullable=False),
        sa.Column('town_hall_level', sa.Integer, nullable=False),
        sa.Column('league', sa.String(25), nullable=True),
        sa.Column('trophies', sa.Integer, nullable=False),
        sa.Column('attack_wins', sa.Integer, nullable=False),
        sa.Column('donations_sent', sa.Integer, nullable=False),
        sa.Column('donations_received', sa.Integer, nullable=False),
        sa.Column('log_date', sa.DateTime,
                  server_default=sa.func.current_timestamp(),
                  nullable=False)
    )


def downgrade() -> None:
    op.drop_table('player_logs')
