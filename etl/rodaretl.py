from etl.etl import ETL

def main():
    origem = 'dados_para_importacao.xlsx' 
    destino = "mssql+pyodbc://sa:impacta1@localhost/parcial?driver=ODBC+Driver+17+for+SQL+Server"

    etl = ETL(origem, destino)

    try:
        etl.extract()
        etl.transform()
        etl.load()
        print("ETL executado com sucesso!")
    except Exception as e:
        print(f"Erro ao executar ETL: {e}")

if __name__ == "__main__":
    main()
