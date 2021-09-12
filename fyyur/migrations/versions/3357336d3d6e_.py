"""empty message

Revision ID: 3357336d3d6e
Revises: 8e01409e21f7
Create Date: 2021-09-12 20:15:43.069982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3357336d3d6e'
down_revision = '8e01409e21f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('show_artist_id_fkey', 'show', type_='foreignkey')
    op.drop_column('show', 'artist_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('show_artist_id_fkey', 'show', 'artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###
