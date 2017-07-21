"""todoist_id added, state modified

Revision ID: 00d31c3cee48
Revises: 8b0b3bbd0cac
Create Date: 2017-07-21 09:26:06.930874

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '00d31c3cee48'
down_revision = '8b0b3bbd0cac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('todoist_id', sa.BigInteger(), nullable=True))
    op.create_index(op.f('ix_user_state'), 'user', ['state'], unique=False)
    op.create_index(op.f('ix_user_todoist_id'), 'user', ['todoist_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_todoist_id'), table_name='user')
    op.drop_index(op.f('ix_user_state'), table_name='user')
    op.drop_column('user', 'todoist_id')
    # ### end Alembic commands ###
