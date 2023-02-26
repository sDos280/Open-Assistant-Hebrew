"""added users table

Revision ID: b365a18db6fd
Revises: 4bead1c4cf52
Create Date: 2023-02-21 22:05:52.620014

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "b365a18db6fd"
down_revision = "4bead1c4cf52"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("provider", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("provider_account_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("display_name", sqlmodel.sql.sqltypes.AutoString(length=256), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_provider"), "user", ["provider"], unique=False)
    op.create_index(op.f("ix_user_provider_account_id"), "user", ["provider_account_id"], unique=False)
    op.create_index("provider", "user", ["provider_account_id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("provider", table_name="user")
    op.drop_index(op.f("ix_user_provider_account_id"), table_name="user")
    op.drop_index(op.f("ix_user_provider"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###