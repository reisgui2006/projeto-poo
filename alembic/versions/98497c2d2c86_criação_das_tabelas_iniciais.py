"""Criação das tabelas iniciais

Revision ID: 98497c2d2c86
Revises: 
Create Date: 2025-05-27 09:49:49.712089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98497c2d2c86'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estado',
    sa.Column('uf', sa.String(length=2), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('uf')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cidade',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('uf', sa.String(length=2), nullable=False),
    sa.ForeignKeyConstraint(['uf'], ['estado.uf'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('empresa_assistencia_tecnica',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('razao_social', sa.String(length=100), nullable=False),
    sa.Column('nome_fantasia', sa.String(length=100), nullable=False),
    sa.Column('cep', sa.String(length=10), nullable=False),
    sa.Column('bairro', sa.String(length=50), nullable=False),
    sa.Column('endereco', sa.String(length=100), nullable=False),
    sa.Column('ddd', sa.String(length=3), nullable=False),
    sa.Column('telefone', sa.String(length=15), nullable=False),
    sa.Column('classificacao', sa.String(length=20), nullable=False),
    sa.Column('cidade_id', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['cidade_id'], ['cidade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('empresa_assistencia_tecnica')
    op.drop_table('cidade')
    op.drop_table('user')
    op.drop_table('estado')
    # ### end Alembic commands ###
