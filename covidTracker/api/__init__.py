import logging
import os

from flask_restplus import Api as _Api
from flask_restplus import reqparse as _reqparse
from werkzeug.exceptions import HTTPException

log = logging.getLogger(__name__)

v = os.popen('git log | head -n 1')
commit = v.read().replace("commit ", "")[:7]

api = _Api(version='0.1#{}'.format(commit), default='',
           title='Covid Tracker', description='Monitoramento de casos do COVID no Brasil.')