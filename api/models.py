from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class CovidAgg(Base):
    __tablename__ = "covid_regiao_periodo"

    data: str = Column(String, primary_key=True, index=True)
    regiao: str = Column(String(100), nullable=False)
    estado: str = Column(String(255), nullable=False)
    uf: str = Column(String(255), nullable=False)
    governador: str = Column(String(255), nullable=False)
    casos_acumulados: int = Column(Integer, nullable=False)
    obitos_acumulados: int = Column(Integer, nullable=False)


class CovidHist(Base):
    __tablename__ = "historico_covid"

    regiao: str = Column(String(255), nullable=False)
    estado: str = Column(String(255), nullable=False)
    municipio: str = Column(String(255), nullable=False)    
    cod_uf: int = Column(Integer, nullable=False, primary_key=True, index=True)
    data: str = Column(String, nullable=False)
    casos_acumulados: int = Column(Integer, nullable=False)
    casos_novos: int = Column(Integer, nullable=False)
    obitos_acumulados: int = Column(Integer, nullable=False)
    obitos_novos: int = Column(Integer, nullable=False)


class Regiao(Base):
    __tablename__ = "regiao"

    codigo_uf: int = Column(Integer, nullable=False, primary_key=True, index=True)
    uf: str = Column(String(255), nullable=False)
    governador: str = Column(String(255), nullable=False)

