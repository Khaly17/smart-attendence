"""Add email, phone, and department columns to User model

Revision ID: 074364f00e52
Revises: 8064f2733331
Create Date: 2024-11-03 08:03:11.525749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '074364f00e52'
down_revision = '8064f2733331'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('phone', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('department', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'department')
    op.drop_column('users', 'phone')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
