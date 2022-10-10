from grpc import Status
from .main import app
from fastapi.testclient import TestClient


client = TestClient(app)



def test_response_struct():
    uf = 'pr'
    data_inicio = '2021-01-01'
    data_final = '2021-01-01'
    response = client.get(f'/hist/{uf}/data_inicio={data_inicio}&data_final={data_final}')
    assert response.json() == [{
            "regiao": "Sul",
            "estado": "Paraná",
            "governador": "CARLOS ROBERTO MASSA JUNIOR",
            "obitos_acumulados": 7993,
            "data": "2021-01-01",
            "uf": "PR",
            "casos_acumulados": 418323
    }]


def test_read_inexistent_uf():
    uf = 'foo_uf'
    data_inicio = '2021-01-01'
    data_final = '2021-01-01'
    response = client.get(f'/hist/{uf}/data_inicio={data_inicio}&data_final={data_final}')
    assert response.status_code == 404


def test_read_invalid_date():
    uf = 'SP'
    data_inicio = '2021-01-01'
    data_final = '0000-00-00'
    response = client.get(f'/hist/{uf}/data_inicio={data_inicio}&data_final={data_final}')
    assert response.status_code == 404


def test_response_status():
    response = client.get('/hist/')
    assert response.status_code  == 200
