"""included the upvotes and down votes

Revision ID: 8e1112c5cfe1
Revises: 60a0f78be642
Create Date: 2020-05-03 21:34:26.467538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e1112c5cfe1'
down_revision = '60a0f78be642'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('downvotes', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('upvotes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'upvotes')
    op.drop_column('users', 'downvotes')
    # ### end Alembic commands ###
