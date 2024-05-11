from flask import Blueprint, jsonify
import requests

from datetime import date

fecha_actual = date.today().strftime('%Y-%m-%d')

def getSeries(plata):
    url = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx"
    parametros = {
        "user": "richarddiaz0107@gmail.com",
        "pass": "A2c9435207.",
        "firstdate": fecha_actual,
        "lastdate": fecha_actual,
        "timeseries": "F073.TCO.PRE.Z.D",
        "function": "GetSeries"
    }
    respuesta = requests.get(url, params=parametros)
    try:
        if respuesta.status_code == 200:
            datos = respuesta.json()['Series']['Obs'][0]['value']
            datoNumerico = float(datos)
            return (plata/datoNumerico)
        else:
            return jsonify(respuesta), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500