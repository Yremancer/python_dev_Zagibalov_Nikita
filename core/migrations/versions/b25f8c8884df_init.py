"""empty message

Revision ID: b25f8c8884df
Revises: 
Create Date: 2026-03-16 00:30:56.566333

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b25f8c8884df'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # main schema tables
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login'),
    sa.UniqueConstraint('email'),
    schema='main'
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['main.users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='main'
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('header', sa.String(length=255), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('blog_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['main.users.id'], ),
    sa.ForeignKeyConstraint(['blog_id'], ['main.blog.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='main'
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['main.users.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['main.post.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='main'
    )
    # logs schema tables
    op.create_table('event_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='logs'
    )
    op.create_table('space_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='logs'
    )
    op.create_table('logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('space_type_id', sa.Integer(), nullable=False),
    sa.Column('event_type_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['event_type_id'], ['logs.event_type.id'], ),
    sa.ForeignKeyConstraint(['space_type_id'], ['logs.space_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='logs'
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('logs', schema='logs')
    op.drop_table('space_type', schema='logs')
    op.drop_table('event_type', schema='logs')
    op.drop_table('comment', schema='main')
    op.drop_table('post', schema='main')
    op.drop_table('blog', schema='main')
    op.drop_table('users', schema='main')
