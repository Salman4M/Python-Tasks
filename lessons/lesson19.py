import requests
import json


api_key = '30d4741c779ba94c470ca1f63045390a'
url = f"https://api.openweathermap.org/data/2.5/weather?q=Baku&units=imperial&APPID={api_key}"


response = requests.get(url=url).json()

# with open("ders.txt", "w") as myfile:
#     myfile.write(f"{response.json()}")
#     myfile.close()


# data = {'coord': {'lon': 49.892, 'lat': 40.3777}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 77.05, 'feels_like': 77.14, 'temp_min': 77.05, 'temp_max': 77.05, 'pressure': 1015, 'humidity': 57}, 'visibility': 10000, 'wind': {'speed': 13.8, 'deg': 30}, 'clouds': {'all': 0}, 'dt': 1685691827, 'sys': {'type': 1, 'id': 8841, 'country': 'AZ', 'sunrise': 1685668353, 'sunset': 1685721868}, 'timezone': 14400, 'id': 587084, 'name': 'Baku', 'cod': 200}


rs = json.dumps(response, indent=4)
print(rs)