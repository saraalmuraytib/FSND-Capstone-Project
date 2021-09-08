"""empty message

Revision ID: f8cf896a5634
Revises: 4dd44d186489
Create Date: 2021-09-08 00:59:21.846293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8cf896a5634'
down_revision = '4dd44d186489'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tutor', sa.Column('availableTime', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tutor', 'availableTime')
    # ### end Alembic commands ###
