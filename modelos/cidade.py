from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from modelos.base import Base

class Cidade(Base.Base, Base):
    __tablename__ = 'cidade'
    id = Column(String(10), primary_key=True)
    nome = Column(String(50), nullable=False)
    uf = Column(String(2), ForeignKey('estado.uf'), nullable=False)

    estado = relationship('Estado', backref='cidades')