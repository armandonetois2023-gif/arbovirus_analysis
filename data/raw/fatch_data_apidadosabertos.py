import requests
import json

def fatch_data(type_disease, year, limit, offset):
    url = f"https://apidadosabertos.saude.gov.br/arboviroses/{type_disease}?nu_ano={year}&limit={limit}&offset={offset}"
    respose = requests.get(url)
    return respose.json()["parametros"] if respose.status_code == 200 else respose.status_code