import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from .abstract_etl import AbstractETL
from modelos.user import User
from modelos.estado import Estado
from modelos.cidade import Cidade
from modelos.empresa_assistencia_tecnica import EmpresaAssistenciaTecnica


class ETL(AbstractETL):
    def __init__(self, origem, destino):
        super().__init__(origem, destino)

    def extract(self):
        try:
            self._dados_extraidos = pd.read_excel(self.origem, sheet_name=None)
        except Exception as e:
            print(f"Erro na extração dos dados: {e}")
            self._dados_extraidos = None

    def transform(self):
        try:
            if self._dados_extraidos is None:
                raise ValueError("Nenhum dado extraído para transformar")
            self._dados_transformados = self._dados_extraidos
        except Exception as e:
            print(f"Erro na transformação dos dados: {e}")
            self._dados_transformados = None

    def load(self):
        if self._dados_transformados is None:
            print("Sem dados para carregar no banco.")
            return

        engine = create_engine(self.destino)
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            if 'user' in self._dados_transformados:
                users_df = self._dados_transformados['user']
                users = User.from_dataframe(users_df)
                session.add_all(users)

            if 'estado' in self._dados_transformados:
                estados_df = self._dados_transformados['estado']
                estados = Estado.from_dataframe(estados_df)
                session.add_all(estados)

            if 'cidade' in self._dados_transformados:
                cidades_df = self._dados_transformados['cidade']
                cidades = Cidade.from_dataframe(cidades_df)
                session.add_all(cidades)

            if 'empresa_assistencia_tecnica' in self._dados_transformados:
                empresas_df = self._dados_transformados['empresa_assistencia_tecnica']
                empresas = EmpresaAssistenciaTecnica.from_dataframe(empresas_df)
                session.add_all(empresas)

            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Erro ao inserir dados no banco: {e}")
        except Exception as e:
            session.rollback()
            print(f"Erro inesperado no carregamento: {e}")
        finally:
            session.close()