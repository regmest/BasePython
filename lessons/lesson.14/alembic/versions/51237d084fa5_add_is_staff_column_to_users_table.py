"""add 'is_staff' column to users table

Revision ID: 51237d084fa5
Revises: 62e7c9f06a05
Create Date: 2021-04-20 19:49:42.005454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51237d084fa5'
down_revision = '62e7c9f06a05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_staff', sa.Boolean(), server_default='FALSE', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_staff')
    # ### end Alembic commands ###
