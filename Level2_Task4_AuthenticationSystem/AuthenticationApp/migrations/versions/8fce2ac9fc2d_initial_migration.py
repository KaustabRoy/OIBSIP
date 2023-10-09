"""Initial Migration

Revision ID: 8fce2ac9fc2d
Revises: 18e5b9c93b76
Create Date: 2023-10-06 22:05:32.430283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fce2ac9fc2d'
down_revision = '18e5b9c93b76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('username')

    # ### end Alembic commands ###
