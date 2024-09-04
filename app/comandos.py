"""
Crearemos los comandos que utilizaremos para la interaccion del usuario y la terminal
"""

import argparse
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables del archivo .env

# Ahora puedes acceder a las variables de entorno
api_key = os.getenv("apikey")
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def api_check(city_name):

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()  # Retorna un dict
    return x


def obtener_comandos():
    parser = argparse.ArgumentParser(
        description="Weathered App - Obtener informacion del clima de una ciudad especifica."
    )  # Creamos el objeto

    parser.add_argument(
        "-c",
        choices=["csv", "json", "txt"],
        required=True,
        help="Elige el formato de la informacion: csv, json, txt",
    )
    parser.add_argument("-n", "--name", required=True, help="Nombre de la cuidad")
    arg = parser.parse_args()
    return arg
