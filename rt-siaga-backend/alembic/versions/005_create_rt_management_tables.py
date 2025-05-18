"""Create RT management tables: profiles, zones, map history

Revision ID: 005
Revises: 004
Create Date: 2025-04-06 10:40:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.create_table(
        "rt_profiles",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("rt_number", sa.String(10), nullable=False, unique=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("map_geojson", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )

    op.create_table(
        "rt_zones",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("profile_id", sa.String(), sa.ForeignKey("rt_profiles.id")),
        sa.Column("zone_name", sa.String(), nullable=False),
        sa.Column("geojson_boundary", sa.Text(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )

    op.create_table(
        "rt_map_history",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("profile_id", sa.String(), sa.ForeignKey("rt_profiles.id")),
        sa.Column("old_geojson", sa.Text(), nullable=True),
        sa.Column("new_geojson", sa.Text(), nullable=False),
        sa.Column("updated_by", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("update_time", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("rt_map_history")
    op.drop_table("rt_zones")
    op.drop_table("rt_profiles")