from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from modelos.base import Base

class EmpresaAssistenciaTecnica(Base.Base, Base):
    __tablename__ = 'empresa_assistencia_tecnica'

    id = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String(100), nullable=False)
    nome_fantasia = Column(String(100), nullable=False)
    cep = Column(String(10), nullable=False)
    bairro = Column(String(50), nullable=False)
    endereco = Column(String(100), nullable=False)
    ddd = Column(String(3), nullable=False)
    telefone = Column(String(15), nullable=False)
    nome_classificacao = Column(String(50), ForeignKey("classificacao.nome"))
    cidade_id = Column(String(10), ForeignKey('cidade.id'), nullable=False)

    cidade = relationship('Cidade', backref='empresas_assistencia')