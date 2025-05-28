from sqlalchemy import Column, String
from modelos.base import Base

class Classificacao(Base.Base, Base):
    __tablename__ = "classificacao"
    nome = Column(String(50), primary_key=True)