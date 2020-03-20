from sqlalchemy import Column, String, Integer, MetaData, Table, DateTime
from covidTracker.api.database import Base, Register, engine

metadata = MetaData()

cases_covid = Table('cases_covid', metadata,
Column('id', Integer, primary_key=True, autoincrement=True),
Column('date', DateTime),
Column('state', String(100)),
Column('suspects',String(100)),
Column('refuses',String(15)),
Column('cases',String(30)),
Column('deaths',String(15)),
Column('recovered',String(30)),
)

all_cases = Table("all_cases", metadata,
Column('id', Integer, primary_key=True, autoincrement=True),
Column('created_at', DateTime),
Column('updated_at', DateTime),
Column('suspects', String(100)),
Column('refuses', String(100)),
Column('cases', String(100)),
Column('deaths', String(100)),
Column('recovered', String(100))
)
