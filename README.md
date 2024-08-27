# Weathered_git

## Objetivo

Un programa que permite obtener información meteorológica de una ciudad específica mediante comandos en la terminal.

## Instalación y Uso

### Versión 0

1. **Instalación de dependencias:**

   Para instalar requests, utiliza el siguiente comando:
   
bash
   pip install requests

   Para instalar `pandas`, utiliza el siguiente comando:
bash
   pip install pandas

### Versión 1
En esta versión, se han añadido comandos para elegir el formato de salida de la información meteorológica: CSV, JSON o TXT.

CSV: Los datos se guardan en un archivo .csv.
JSON: Los datos se guardan en un archivo .json.
TXT: Los datos se guardan en un archivo .txt.

2. **Metodo de uso:**

    Para ejecutar el programa, utiliza el siguiente comando en la terminal:
   
bash    
    python main.py -n <nombre_ciudad> -c <formato>

    Donde:
    -n o --name: Nombre de la ciudad para obtener la información meteorológica.
    -c: Formato de la información: csv, json, txt.
