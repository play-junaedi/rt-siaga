"""Create role_permissions table

Revision ID: 009
Revises: 008
Create Date: 2025-04-09 10:10:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.create_table(
        "role_permissions",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("role_id", sa.String(), sa.ForeignKey("roles.id")),
        sa.Column("permission_id", sa.String(), sa.ForeignKey("permissions.id")),
        sa.Column("assigned_by", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("assigned_at", sa.DateTime(), server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table("role_permissions")