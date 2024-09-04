import pandas, json, csv
from app.comandos import api_check


class Wheather:
    @staticmethod
    def data(city_name):
        """Interactua con la API y extrae datos relevantes del clima para el usuario"""
        x = api_check(city_name)
        datos = pandas.json_normalize(x)

        if x["cod"] != "404":
            data = []
            ciudad = datos["name"][0]
            temperatura = datos["main.temp"][0]  # Temperatura en kelvin
            descripcion_clima = datos["weather"][0][0][
                "description"
            ]  # Extraer el primer elemento de la lista de clima
            pais = datos["sys.country"][0]
            temp_celsius = temperatura - 273.15
            data.append(
                {
                    "ciudad": ciudad,
                    "pais": pais,
                    "kelvin": f"{temperatura} K",
                    "celsius": f"{int(temp_celsius)} °C",
                    "info": descripcion_clima,
                }
            )
            return data
        else:
            print(" City Not Found ")
            return None

    @staticmethod
    def ver_json(city_name):
        datos = Wheather.data(city_name)

        if datos:
            with open("output.json", "+a") as json_file:
                json_data = json.JSONEncoder().encode(datos)
                json_file.write(json_data)

            for elemento in datos:
                print(json.dumps(elemento, indent=2, ensure_ascii=False))

    @staticmethod
    def txt(city_name):
        datos = Wheather.data(city_name)

        if datos:
            # Abrir archivo en modo escritura
            with open("output.txt", "+a", encoding="utf-8") as txt_file:
                for elemento in datos:
                    txt_file.write(f"Ciudad: {elemento['ciudad']}\n")
                    txt_file.write(f"País: {elemento['pais']}\n")
                    txt_file.write(
                        f"Temperatura actual (Kelvin): {elemento['kelvin']}\n"
                    )
                    txt_file.write(
                        f"Temperatura actual (Celsius): {elemento['celsius']}\n"
                    )
                    txt_file.write(f"Descripción del clima: {elemento['info']}\n")
                    txt_file.write("\n")  # Añadir una línea en blanco entre registros
            archivo = open("output.txt", encoding="utf-8")
            print(archivo.read())
            print("Datos guardados en 'output.txt'.")

    @staticmethod
    def export_csv(city_name):
        datos = Wheather.data(city_name)

        if datos:

            nombres_columnas = ["ciudad", "pais", "kelvin", "celsius", "info"]

            with open("outpout.csv", "a", newline="", encoding="utf-8") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=nombres_columnas)

                if csv_file.tell() == 0:
                    writer.writeheader()

                for elementos in datos:
                    print(elementos)
                    writer.writerow(elementos)

            print("Datos guardados en 'output.csv'.")
