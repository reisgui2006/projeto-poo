from sqlalchemy import Column, String
from modelos.base import Base

class Estado(Base.Base, Base):
    __tablename__ = 'estado'
    uf = Column(String(2), primary_key=True)
    nome = Column(String(50), nullable=False)