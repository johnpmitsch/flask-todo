"""empty message

Revision ID: 4cb912ff2d2
Revises: e2d56f3475
Create Date: 2015-02-18 18:36:51.473930

"""

# revision identifiers, used by Alembic.
revision = '4cb912ff2d2'
down_revision = 'e2d56f3475'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('complete_by', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'complete_by')
    ### end Alembic commands ###
