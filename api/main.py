from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from fastapi import Depends, FastAPI, HTTPException, status

from api.models import CovidAgg


## Create engine and db session
my_database_connection = "mysql+pymysql://user:password@localhost/hurb_challenge"
engine = create_engine(my_database_connection)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/hist/")
def home(db:Session = Depends(get_db)):
    return db.query(CovidAgg).all()


@app.get("/hist/{uf}/data_inicio={data_incio}&data_final={data_final}")
def covid_agg(uf:str, data_incio:str, data_final:str, db:Session = Depends(get_db)):
    data = db.query(CovidAgg).filter(CovidAgg.uf == uf, 
                                          CovidAgg.data >= data_incio,
                                          CovidAgg.data <= data_final).all()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid inputs"
        )
    return data