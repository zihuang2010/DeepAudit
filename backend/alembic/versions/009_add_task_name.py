"""add task_name to audit_tasks

Revision ID: 009_add_task_name
Revises: 008_add_files_with_findings
Create Date: 2026-01-04
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '009_add_task_name'
down_revision = '008_add_files_with_findings'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 添加 task_name 字段到 audit_tasks 表
    op.add_column('audit_tasks', sa.Column('task_name', sa.String(100), nullable=True))


def downgrade() -> None:
    op.drop_column('audit_tasks', 'task_name')
