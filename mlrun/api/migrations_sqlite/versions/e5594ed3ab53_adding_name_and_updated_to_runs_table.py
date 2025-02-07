"""Adding name and updated to runs table

Revision ID: e5594ed3ab53
Revises: accf9fc83d38
Create Date: 2022-01-08 12:33:59.070265

"""
import datetime

import sqlalchemy as sa
from alembic import op

import mlrun.api.utils.db.sql_collation

# revision identifiers, used by Alembic.
revision = "e5594ed3ab53"
down_revision = "accf9fc83d38"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("runs") as batch_op:
        batch_op.add_column(
            sa.Column(
                "name",
                sa.String(
                    length=255,
                    collation=mlrun.api.utils.db.sql_collation.SQLCollationUtil.collation(),
                ),
                default="no-name",
            )
        )
        batch_op.add_column(
            sa.Column(
                "updated", sa.String(length=255), default=datetime.datetime.utcnow
            )
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("runs") as batch_op:
        batch_op.drop_column("name")
        batch_op.drop_column("updated")
    # ### end Alembic commands ###
