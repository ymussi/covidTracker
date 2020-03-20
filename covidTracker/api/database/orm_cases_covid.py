from sqlalchemy import Column, String, Integer, MetaData, Table, DateTime
from covidTracker.api.database import Base, Register

class CasesCovid(Base, Register):

    __tablename__ = "cases_covid"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    state = Column(String(100))
    suspects = Column(String(100))
    refuses = Column(String(15))
    cases = Column(String(30))
    deaths = Column(String(15))
    recovered = Column(String(30))

class AllCasesCovid(Base, Register):

    __tablename__ = "all_cases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    update_at = Column(DateTime)
    suspects = Column(String(100))
    refuses = Column(String(100))
    cases = Column(String(100))
    deaths = Column(String(100))
    recovered = Column(String(100))
