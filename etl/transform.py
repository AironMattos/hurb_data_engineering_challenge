import apache_beam as beam
import os
from sqlalchemy import create_engine
from zipfile import ZipFile


# Unzip data
with ZipFile('./data/raw/Desafio Data Engineer - Arquivos.zip') as zip:
    for zip_info in zip.infolist():
        if zip_info.filename[-1] == '/':
            continue
        zip_info.filename = os.path.basename(zip_info.filename)
        zip.extract(zip_info, 'data/raw/')


#Apache Beam Pipelines
def estados_ibge():
    pipe = beam.Pipeline()
    header = 'codigo_uf;uf;governador'

    (
        pipe
        #|beam.io.ReadFromText(r'D:\Engenharia_de_Dados\desafio_hurb\data\raw\EstadosIBGE.csv', skip_header_lines=1)
        |beam.io.ReadFromText('./data/raw/EstadosIBGE.csv', skip_header_lines=1)
        |beam.Map(lambda record: record.split(';'))
        |beam.Map(lambda record: tuple([record[1], record[0], record[3]]))
        |beam.Map(lambda record: record[0] + ';' + record[1] + ';' + record[2])
        |beam.io.WriteToText('data/refined/refined_EstadosIBGE',  file_name_suffix='.csv', header=header)
    )

    pipe.run()


def hist_covid():
    pipe = beam.Pipeline()
    header = 'regiao;estado;municipio;cod_uf;data;casos_acumulados;casos_novos;obitos_acumulados;obitos_novos'


    (
        pipe
        #|beam.io.ReadFromText(r'D:\Engenharia_de_Dados\desafio_hurb\data\raw\HIST_PAINEL_COVIDBR.csv', skip_header_lines=1)
        |beam.io.ReadFromText('./data/raw/HIST_PAINEL_COVIDBR.csv', skip_header_lines=1)
        |beam.Map(lambda record: record.split(';'))
        |beam.Map(lambda record: tuple([ record[0], record[1], record[2], record[3], record[7], record[10], record[11], record[12], record[13]]))
        |beam.Map(lambda record:  record[0] + ';' + record[1] + ';' + record[2] + ';' + record[3] + ';' + record[4] + ';' + 
                        record[5] + ';' + record[6] + ';' + record[7] + ';' + record[8])
        |beam.io.WriteToText('data/refined/refined_hist_covid',  file_name_suffix='.csv', header=header)
    )

    pipe.run()
