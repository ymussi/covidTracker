#!/usr/bin/env python
import configparser as _configparser
from os import getenv as _getenv
from os import path as _path
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine

config_dir = _path.dirname(__file__)
env = _getenv('DBENV', 'development')
env = (env if env != "" else 'development')

Config = _configparser.ConfigParser()
Config.read(_path.join(config_dir, 'production', 'config.ini'))

def mysql_engine(schema, pool_size=1, max_overflow=25):
    dbname = Config.get("schema", schema)
    con_str = Config.get("database", dbname)
    engine = create_engine("mysql+pymysql://{}/{}".format(con_str, schema),
                           pool_size=pool_size, max_overflow=max_overflow, pool_recycle=30 * 60)
    return engine

class SQLDBContext(object):
    
    def __init__(self, engine):
        self.session = None
        self.engine = engine

    def __enter__(self):
        session = sessionmaker()
        self.session = session(bind=self.engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.rollback()
        self.session.close()
        
class CadastroDBContext(SQLDBContext):

    def __init__(self, engine):
        super().__init__(engine)