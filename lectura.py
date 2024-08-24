import pandas 
from main import api_check

def data():
    x = api_check()
    datos = pandas.json_normalize(x)

    print(datos['name'])
    print(datos['main.temp'])
    print(datos['weather'][0][0])
    print(datos['sys.country'])
    # print(datos.head())

    if x["cod"] != "404":
        data = []
        ciudad = datos['name'][0]
        temperatura = datos['main.temp'][0] # Temperatura en kelvin
        descripcion_clima = datos['weather'][0][0]['description']  # Extraer el primer elemento de la lista de clima
        pais = datos['sys.country'][0]
        temp_celsius = temperatura - 273.15
        data.append(f"Ciudad: {ciudad}")
        data.append(f"Pais: {pais}")
        data.append(f"Temperatura actual: {temperatura} Kelvin")
        data.append(f"Temperatura actual: {int(temp_celsius)} celsius")
        data.append(f"Descripcion del clima: {descripcion_clima}")
        return data
    else:
        print(" City Not Found ")
