# hurb_data_engineering_challenge

Repositório com a solução para o desafio técnico de data engineer na Hurb.

Nesse desafio, o intuíto foi de coletar bases de dados .csv a respeito da COVID-19, tratá-las, persistir-las em um banco de dados MySQL e posteriormente, disponibilzar os dados via API para consulta. Foram utilizadas diferentes ferramentas para realização da entrega como, por exemplo, Apache Beam para os pipelines de dados e FastAPI para construção da API.


A ideia de resolução girou em torno de extrair os dados do arquivo .zip previamente disponibilizado, tratá-los com o Apache Beam e carregá-los para um banco de dados se utilizando da biblioteca SQLAlchemy como ORM. Após relização da carga para o banco de dados, este mesmo passou a ser requerido por uma API onde, informando parâmetros, é possível consultar dados da COVID separados por estado e também por data.


# Como Utilizar
 
1. Clonando repositório para sua máquina
```bash
git clone https://github.com/AironMattos/hurb_data_engineering_challenge.git
```

2. Abrindo projeto
```bash
cd hurb_data_engineering_challenge
```

3. Criando e ativando ambiente virtual (via PowerShell)
```bash
python -m venv venv

./venv/Scripts/Activate.ps1
```

4. Instalando pacotes necessários
```bash
pip install -r requirements.txt
```

5. Subindo container docker
```bash
docker-compose up
```

6. Rodando pipelines
```bash
python main.py
```

7. Rodando API
```bash
uvicorn api.main:app --reload
```


# API

## Endpoints
Dados COVID separados por estado e período de tempo 

Parametros:
  {uf}
  {data_inicio)
  {data_fim}

```bash
/hist/{uf}/data_inicio={data_incio}&data_final={data_final}
```


Dados COVID histórico geral
```bash
/hist/
```


# Soluções Consultas SQL
 ## Todas as queries geradas encontram-se documentadas no arquivo 'queries.sql'
    
    Qual foi o total de casos de covid por região?
      Sudeste - 1095756068 casos
      Nordeste - 806546103 casos
      Sul - 468503205 casos
      Norte - 381972389 casos
      Centro-Oeste - 345009647 casos
    
    Qual UF foi mais impactada por novos casos de covid em Agosto de 2020?
      São Paulo - 524076 casos
    
    Quais regiões tiveram as maiores quantidade de óbitos em Setembro de 2020?
      Sudeste - 3610310 óbitos
      Nordeste - 2234748 óbitos
      Norte	859510 - óbitos
      Centro-Oeste - 666220 óbitos
      Sul	- 639704 óbitos
      
    Qual foi o ranking de novos casos por governador no 4T de 2020?
      JOÃO AGRIPINO DA COSTA DORIA JUNIOR - 953338 casos
      CARLOS MOISÉS DA SILVA - 554210 casos
      EDUARDO FIGUEIREDO CAVALHEIRO LEITE -	518204 casos
      ROMEU ZEMA NETO	- 495480 casos
    
    Qual está sendo a 3a Região mais afetada por novos óbitos em 2021?
      Nordeste - 24820 óbitos
    
    
 



