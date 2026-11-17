import requests
from pprint import pprint

def consultar_clima():
    url = "http://127.0.0.1:8000/v1/forecast?latitude=-26.4851&longitude=-49.0713"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        
        dados = resposta.json()
        
        temperatura = dados["current"]["temperature_2m"]
        umidade = dados["current"]["relative_humidity_2m"]
        sens_termica = dados["current"]["apparent_temperature"]
        precipitacao = dados["current"]["precipitation"]
        vel_vento = dados["current"]["wind_speed_10m"]
        hora = dados["current"]["time"]
        local = dados["timezone"]

        print(f"A temperatura atual é: {temperatura}°C")
        print(f"A umidade atual é: {umidade}%")
        print("")
        print(f"A sensação térmica é: {sens_termica}°C")
        print(f"O nível de precipitação é: {precipitacao}mm")
        print(f"A velocidade do vento é: {vel_vento}km/h")
        print("")
        print(f"O horário atual é: {hora}")
        print(f"Local da leitura: {local}")

        return dados
    else:
        print(f"Algo deu errado: {resposta.status_code}")


consultar_clima()