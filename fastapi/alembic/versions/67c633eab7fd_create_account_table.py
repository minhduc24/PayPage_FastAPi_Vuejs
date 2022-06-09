"""create account table

Revision ID: 67c633eab7fd
Revises: 
Create Date: 2022-06-07 15:31:04.091733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67c633eab7fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))
    
def downgrade():
    op.drop_table('account')
