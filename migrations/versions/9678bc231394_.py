"""empty message

Revision ID: 9678bc231394
Revises: 
Create Date: 2020-09-30 11:56:09.746965

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9678bc231394'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('batteries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('serial_number', sa.String(length=100), nullable=False),
    sa.Column('capacity', sa.Float(), nullable=False),
    sa.Column('energy_level', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('serial_number')
    )
    op.create_table('motorcycles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('serial_number', sa.String(length=100), nullable=False),
    sa.Column('odometer', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('serial_number')
    )
    op.create_table('stations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(length=250), nullable=False),
    sa.Column('number_of_batteries', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location'),
    sa.UniqueConstraint('number_of_batteries')
    )
    op.create_table('drivers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('license_number', sa.String(length=100), nullable=False),
    sa.Column('motorcycle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['motorcycle_id'], ['motorcycles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('license_number'),
    sa.UniqueConstraint('name')
    )
    op.create_table('swaps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('driver_id', sa.Integer(), nullable=False),
    sa.Column('station_id', sa.Integer(), nullable=False),
    sa.Column('old_battery', postgresql.JSON(astext_type=sa.Text()), nullable=False),
    sa.Column('new_battery', postgresql.JSON(astext_type=sa.Text()), nullable=False),
    sa.Column('distance_covered', sa.Float(), nullable=False),
    sa.Column('energy_used', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['driver_id'], ['drivers.id'], ),
    sa.ForeignKeyConstraint(['station_id'], ['stations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('swaps')
    op.drop_table('drivers')
    op.drop_table('stations')
    op.drop_table('motorcycles')
    op.drop_table('batteries')
    # ### end Alembic commands ###
