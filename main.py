import requests

apikey = "82166bf06774ec63a7b31774f9652660"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def api_check():
    city_name = input("Enter city name : ")

    complete_url = base_url + "appid=" + apikey + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json() # Retorna un dict
    return x

