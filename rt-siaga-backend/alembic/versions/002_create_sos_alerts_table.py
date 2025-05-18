"""Create sos_alerts table

Revision ID: 002
Revises: 001
Create Date: 2025-04-06 10:10:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.create_table(
        "sos_alerts",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("location_lat", sa.String(), nullable=False),
        sa.Column("location_lng", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("triggered_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("resolved", sa.Boolean(), default=False),
        sa.Column("resolved_by", sa.String(), sa.ForeignKey("users.id"), nullable=True),
        sa.Column("resolved_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("sos_alerts")