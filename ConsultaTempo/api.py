import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc


chave_api = "a94117987ef6b55c1bc18ba716a0da6b"
cidade = 'Bangalore'
api_link =f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br"


r = requests.get(api_link)

dados = r.json()
 

pais_codigo = dados['sys']['country']


fuso_horario = pytz.country_timezones[pais_codigo]


pais = pytz.country_names[pais_codigo] 


zona = pytz.timezone(fuso_horario[0])
zona_horas = datetime.now(zona)
zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")



tempo = dados['main']['temp']
pressao = dados['main']['pressure']
umidade = dados['main']['humidity']
velocidade = dados['wind']['speed']
descricao = dados['weather'][0]['description']




def pais_to_continente(p):
    pais_alpha = pc.country_name_to_country_alpha2(p)
    pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
    pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)
    
    return pais_continente_nome

continente = pais_to_continente(pais)

print(continente)

codigo_pais = pc.country_name_to_country_alpha2("China", cn_name_format="default")
continente_nome = pc.country_alpha2_to_continent_code(codigo_pais)
