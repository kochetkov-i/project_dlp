"""empty message

Revision ID: 41dc7c5def3e
Revises: c92b2d8834bc
Create Date: 2021-10-09 15:39:31.315777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41dc7c5def3e'
down_revision = 'c92b2d8834bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('userrole', sa.String(length=32), nullable=True))
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('users', 'usersurname',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('users', 'useremail',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'useremail',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('users', 'usersurname',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.drop_column('users', 'userrole')
    # ### end Alembic commands ###
