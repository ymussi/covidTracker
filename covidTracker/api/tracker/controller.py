from covidTracker.api.config import Config, CadastroDBContext
from covidTracker.api.database import engine
from covidTracker.api.database.orm_cases_covid import CasesCovid
from covidTracker.api.database.orm_create_db import metadata
from datetime import datetime, timedelta

import requests, json

class Cases():

    def __init__(self):
        self.URL_MS = Config.get('URD_MS', 'url')

    def get_cases(self):
        request = requests.get(self.URL_MS)

        content = request.content.decode('utf8').replace('var database=', '')
        data = json.loads(content)

        return data

    def depara_estados(self, uid):
        try:
            depara = {
                "11": 'Rondônia',
                "12": 'Acre', 
                "13": 'Amazonas',
                "14": 'Roraima',
                "15": 'Pará',
                "16": 'Amapá', 
                "17": 'Tocantins',
                "21": 'Maranhão',
                "22": 'Piauí',
                "23": 'Ceará',
                "24": 'Rio Grande do Norte',
                "25": 'Paraíba',
                "26": 'Pernambuco',
                "27": 'Alagoas',
                "28": 'Sergipe',
                "29": 'Bahia',
                "31": 'Minas Gerais',
                "32": 'Espírito Santo',
                "33": 'Rio de Janeiro',
                "35": 'São Paulo',
                "41": 'Paraná',
                "42": 'Santa Catarina',
                "43": 'Rio Grande do Sul',
                "50": 'Mato Grosso do Sul',
                "51": 'Mato Grosso',
                "52": 'Goiás',
                "53": 'Distrito Federal'
                }
                
            estado = depara[str(uid)]
            return estado
        except:
            return uid            

    def format_cases(self):
        data = self.get_cases()
        
        all_cases = []
        for record in data['brazil']:
            date_time = datetime.strptime(f"{record['date']} {record['time']}",
                                          '%d/%m/%Y %H:%M')
            cases = []
            for value in record['values']:
                state = self.depara_estados(value['uid'])
                case = {
                    "date": str(date_time),
                    "state": state,
                    "suspects":  value.get('suspects', 0),
                    "refuses":  value.get('refuses', 0),
                    "cases":  value.get('cases', 0),
                    "deaths":  value.get('deaths', 0),
                    "recovered":  value.get('recovered', 0)
                }
                cases.append(case)

            all_cases.append(cases)

        self.save_cases(all_cases)
        return all_cases

    def save_cases(self, all_cases):
        date_now = datetime.now()
        two_days_ago = date_now - timedelta(days=2)
        new_date = two_days_ago.strftime('%Y-%m-%d %H:%M:%s')
        try:
            if all_cases is None:
                return {"status": False, "msg": "não obtivemos atualizações."}
            else:
                metadata.drop_all(engine)
                metadata.create_all(engine)
                for cases in all_cases:
                    for case in cases:
                        if case['date'] >= new_date:
                            with CadastroDBContext(engine) as db:
                                cas = CasesCovid(**case)
                                db.session.add(cas)
                                db.session.commit()
                return {"status": True, "msg": "Casos cadastrados com sucesso."}
        except Exception as e:
            return {"status": False, "msg": e}

if __name__ == "__main__":
    r = Cases()
    # res = r.format_cases()
    res = r.save_cases()
    print(res)