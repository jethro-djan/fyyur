"""empty message

Revision ID: 1dd6eac60351
Revises: 5ecc019f6ee4
Create Date: 2021-09-12 22:47:01.734158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dd6eac60351'
down_revision = '5ecc019f6ee4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('genre', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'genre', 'venue', ['venue_id'], ['id'])
    op.create_unique_constraint(None, 'venue_profiles', ['venue_id', 'genre_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'venue_profiles', type_='unique')
    op.drop_constraint(None, 'genre', type_='foreignkey')
    op.drop_column('genre', 'venue_id')
    # ### end Alembic commands ###
