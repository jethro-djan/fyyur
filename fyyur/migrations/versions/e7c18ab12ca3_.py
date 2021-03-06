"""empty message

Revision ID: e7c18ab12ca3
Revises: 84bfb729d1ec
Create Date: 2021-09-11 05:27:41.455383

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e7c18ab12ca3'
down_revision = '84bfb729d1ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artist', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('genre', 'name',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('show', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('venue', 'name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venue', 'name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('show', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('genre', 'name',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('artist', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
