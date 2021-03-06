"""state, is_active, last_active_at fields added

Revision ID: 8b0b3bbd0cac
Revises: 8ca2c1eef1b2
Create Date: 2017-07-21 05:04:58.336792

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '8b0b3bbd0cac'
down_revision = '8ca2c1eef1b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('last_active_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('state', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column('state')
        batch_op.drop_column('last_active_at')
        batch_op.drop_column('is_active')
        # ### end Alembic commands ###
