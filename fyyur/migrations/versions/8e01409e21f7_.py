"""empty message

Revision ID: 8e01409e21f7
Revises: 29df01b0d3a5
Create Date: 2021-09-12 20:13:50.193443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e01409e21f7'
down_revision = '29df01b0d3a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artist_profiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist_profiles',
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='artist_profiles_artist_id_fkey'),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name='artist_profiles_genre_id_fkey'),
    sa.PrimaryKeyConstraint('artist_id', 'genre_id', name='artist_profiles_pkey')
    )
    # ### end Alembic commands ###
