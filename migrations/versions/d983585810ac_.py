"""empty message

Revision ID: d983585810ac
Revises: 81a713eded64
Create Date: 2017-01-12 03:11:22.255702

"""

# revision identifiers, used by Alembic.
revision = 'd983585810ac'
down_revision = '81a713eded64'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('discount_codes', 'value',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('discount_codes', 'value',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    ### end Alembic commands ###
