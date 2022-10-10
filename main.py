from etl.extract import unzip_data
from etl.transform import estados_ibge, hist_covid
from etl.load import DatabaseOperations
from etl.load import query


def etl():
    # Extract data from zip file
    unzip_data('./data/raw/Desafio Data Engineer - Arquivos.zip')

    # Transform data with apache beam
    estados_ibge()
    hist_covid()

    # Load data to database
    load = DatabaseOperations()
    load.csv_to_table('./data/refined/refined_EstadosIBGE-00000-of-00001.csv', 'regiao')
    load.csv_to_table('./data/refined/refined_hist_covid-00000-of-00001.csv', 'historico_covid')
    load.query_to_table(query, 'covid_regiao_periodo')


if __name__ == '__main__':
    #######
    print('Processing data')
    print('---------------')
    ########
    etl()
    ########
    print('Processing completed')