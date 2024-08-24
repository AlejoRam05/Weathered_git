import json
from lectura import data

data = data()

# Escribir el JSON a un archivo .txt
with open('output.txt', 'w') as txt_file:
    json.dump(data, txt_file, indent=4)

print("JSON ha sido convertido a un archivo .txt")
