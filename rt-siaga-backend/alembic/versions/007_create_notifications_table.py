"""Create notifications table

Revision ID: 007
Revises: 006
Create Date: 2025-04-08 13:00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '007'
down_revision: Union[str, None] = '006'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "notifications",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("type", sa.Enum("sos", "pengumuman", "forum", name="notification_types"), nullable=False),
        sa.Column("read_status", sa.Boolean(), default=False),
        sa.Column("sent_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("notifications")
    sa.Enum(name="notification_types").drop(op.get_bind())