"""empty message

Revision ID: 09c0cd8f61b8
Revises: 
Create Date: 2022-06-16 18:41:22.003739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09c0cd8f61b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('musician',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('e_mail', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.Column('introduction', sa.String(length=120), nullable=True),
    sa.Column('avatar_link', sa.String(), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('introduction', sa.String(length=120), nullable=True),
    sa.Column('cover_link', sa.String(), nullable=True),
    sa.Column('song_link', sa.String(length=500), nullable=True),
    sa.Column('genre', sa.String(length=120), nullable=True),
    sa.Column('musician_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['musician_id'], ['musician.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song')
    op.drop_table('musician')
    # ### end Alembic commands ###
