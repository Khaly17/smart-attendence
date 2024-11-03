"""Add status column to Attendance

Revision ID: 3f4bbdfb285f
Revises: f4f55d383767
Create Date: 2024-11-02 23:12:58.671008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f4bbdfb285f'
down_revision = 'f4f55d383767'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attendances', sa.Column('status', sa.String(length=20), nullable=False, server_default='Present'))
    # ### end Alembic commands ###
    op.alter_column('attendances', 'status', server_default=None)



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('attendances', 'status')
    # ### end Alembic commands ###