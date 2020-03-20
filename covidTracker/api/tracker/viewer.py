from covidTracker.api.tracker.controller import Cases
from flask_restplus import Resource
from flask import request
from covidTracker.api import api
import logging

log = logging.getLogger(__name__)

ns = api.namespace('cases', description='Busca casos fornecidos pelo Ministério da Saúde.')

@ns.route('/listar')
class Listar(Resource):
    def get(self):

        c = Cases()
        res = c.format_cases()

        return res