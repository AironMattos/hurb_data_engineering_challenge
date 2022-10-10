from sqlalchemy import create_engine
import pandas as pd


class DatabaseOperations():
    def __init__(self) -> None:
        self.mysql_engine = create_engine('mysql+pymysql://user:password@localhost/hurb_challenge')


    def csv_to_table(self, file, table_name):
        data = pd.read_csv(file, sep=';')
        data.to_sql(table_name, self.mysql_engine, index=False)


    def query_to_table(self, query, table_name):
        df = pd.read_sql(query, con=self.mysql_engine)
        df.to_sql(table_name, self.mysql_engine, index=False)
    



# Query to create 'covid_regiao_periodo' table 
query = '''SELECT 
        t2.data,
        t2.regiao,
        t2.estado,
        t1.uf,
        t1.governador,
        t2.casos_acumulados,
        t2.obitos_acumulados
    FROM
        regiao as t1
    JOIN
        historico_covid as t2
    WHERE 
        t2.cod_uf = t1.codigo_uf'''



