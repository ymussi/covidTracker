#!/usr/bin/env python
from sqlalchemy.ext.declarative import declarative_base
from covidTracker.api.config import mysql_engine
from datetime import datetime
from sqlalchemy import inspect

Base = declarative_base()
engine = mysql_engine("controleCovid")


class Register():
    def to_dict(self):
            result = {}
            for c in inspect(self).mapper.column_attrs:
                field = getattr(self, c.key)
                # Verificar o tipo do campo
                if type(field) == datetime.date:
                    field = datetime.strftime('%Y-%m-%d', field)
                result[c.key] = field
            return result