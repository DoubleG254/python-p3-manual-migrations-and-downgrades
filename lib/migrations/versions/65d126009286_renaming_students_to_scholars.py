"""Renaming students to scholars

Revision ID: 65d126009286
Revises: 791279dd0760
Create Date: 2023-09-11 12:50:52.494337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65d126009286'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students","scholars")
    pass


def downgrade() -> None:
    op.rename_table("scholars","students")
    pass
