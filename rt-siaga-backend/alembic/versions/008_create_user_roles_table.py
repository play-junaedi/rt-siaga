"""Create user_roles table

Revision ID: 008
Revises: 007
Create Date: 2025-04-09 10:00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.create_table(
        "user_roles",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("role_id", sa.String(), sa.ForeignKey("roles.id")),
        sa.Column("assigned_at", sa.DateTime(), server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table("user_roles")