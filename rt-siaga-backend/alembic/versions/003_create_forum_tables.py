"""Create questions & answers tables

Revision ID: 003
Revises: 002
Create Date: 2025-04-06 10:20:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.create_table(
        "questions",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("question_text", sa.Text(), nullable=False),
        sa.Column("category", sa.String(), nullable=True),
        sa.Column("posted_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column("answered", sa.Boolean(), default=False),
    )

    op.create_table(
        "answers",
        sa.Column("id", sa.String(), nullable=False, primary_key=True),
        sa.Column("question_id", sa.String(), sa.ForeignKey("questions.id")),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id")),
        sa.Column("answer_text", sa.Text(), nullable=False),
        sa.Column("is_best_answer", sa.Boolean(), default=False),
        sa.Column("posted_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("answers")
    op.drop_table("questions")