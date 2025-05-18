"""Create ACL tables: roles, permissions, role_permissions, user_permissions

Revision ID: 004
Revises: 003
Create Date: 2025-04-06 10:30:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.create_table(
        "roles",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("name", sa.String(), unique=True, nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )

    op.create_table(
        "permissions",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("name", sa.String(), unique=True, nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )

    op.create_table(
        "role_permissions",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("role_id", sa.String(), sa.ForeignKey("roles.id")),
        sa.Column("permission_id", sa.String(), sa.ForeignKey("permissions.id")),
        sa.Column("assigned_by", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("assigned_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )

    op.create_table(
        "login_history",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("ip_address", sa.String(), nullable=False),
        sa.Column("device_info", sa.String(), nullable=False),
        sa.Column("success", sa.Boolean(), default=False),
        sa.Column("login_time", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )

    op.create_table(
        "password_reset_tokens",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("token", sa.String(), unique=True, index=True, nullable=False),
        sa.Column("expires_at", sa.DateTime(), server_default=sa.func.now() + sa.text("'30 minutes'::interval")),
        sa.Column("used", sa.Boolean(), default=False),
    )


def downgrade() -> None:
    op.drop_table("password_reset_tokens")
    op.drop_table("login_history")
    op.drop_table("role_permissions")
    op.drop_table("permissions")
    op.drop_table("roles")