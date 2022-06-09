"""Add a column

Revision ID: 076640dc0afe
Revises: 67c633eab7fd
Create Date: 2022-06-07 15:49:23.179952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '076640dc0afe'
down_revision = '67c633eab7fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    
    insp = inspect(conn)
    fk_names = [fk['name'] for fk in insp.get_foreign_keys('host')]
    if ("fk_hypervisor_id_resource_id" not in fk_names and
            "fk_host_id_resource_id" in fk_names):
        # NOTE(sileht): we are already good, the BD have been created from
        # scratch after "a54c57ada3f5"
        return

    op.drop_constraint("fk_hypervisor_id_resource_id", "host",
                       type_="foreignkey")
    op.drop_constraint("fk_hypervisor_history_resource_history_revision",
                       "host_history", type_="foreignkey")
    op.create_foreign_key("fk_host_id_resource_id", "host", "resource",
                          ["id"], ["id"], ondelete="CASCADE")
    op.create_foreign_key("fk_host_history_resource_history_revision",
                          "host_history", "resource_history",
                          ["revision"], ["revision"], ondelete="CASCADE") 


def downgrade() -> None:
    pass
