"""Create users table

Revision ID: 001
Revises: 
Create Date: 2025-04-06 10:00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), unique=True, index=True, nullable=False),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("password_hash", sa.String(), nullable=False),
        sa.Column("role", sa.Enum("warga", "rt", "rw", "admin", name="user_roles"), nullable=False),
        sa.Column("status", sa.Enum("aktif", "nonaktif", "pending", name="user_status"), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
    sa.Enum(name="user_roles").drop(op.get_bind())
    sa.Enum(name="user_status").drop(op.get_bind())