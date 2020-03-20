from sqlalchemy import Column, String, Integer, MetaData, Table, DateTime
from covidTracker.api.database import Base, Register, engine

metadata = MetaData()

cadastro = Table('cases_covid', metadata,
Column('id', Integer, primary_key=True, autoincrement=True),
Column('date', DateTime),
Column('state', String(100)),
Column('suspects',String(100)),
Column('refuses',String(15)),
Column('cases',String(30)),
Column('deaths',String(15)),
Column('recovered',String(30)),
)

# metadata.create_all(engine)