"""transactions v2.1

Revision ID: 1a3888629738
Revises: 711b327cdf9b
Create Date: 2021-11-09 11:16:58.451680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a3888629738'
down_revision = '711b327cdf9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('collections_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'transactions', 'collections', ['collections_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'transactions', type_='foreignkey')
    op.drop_column('transactions', 'collections_id')
    # ### end Alembic commands ###
