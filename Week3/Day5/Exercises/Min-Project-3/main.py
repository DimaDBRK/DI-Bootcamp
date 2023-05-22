import pyowm
owm = pyowm.OWM('d4eec5827258a09c413b3e60d50c6a5d')

print("Weather")
weather_mgr = owm.weather_manager()
place = 'Tel Aviv, IL'
observation = weather_mgr.weather_at_place(place)
print(observation.weather)
temperature = observation.weather.temperature("celsius")["temp"]
humidity = observation.weather.humidity
wind = observation.weather.wind()
print(f'Temperature: {temperature}°C')
print(f'Humidity: {humidity}%')
print(f'Wind Speed: {wind["speed"]} m/s')

print("Get city")
import requests
s_city = "Tel Aviv"
city_id = 0
appid = "d4eec5827258a09c413b3e60d50c6a5d"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': appid})
    data = res.json()
    print(data)
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
    print("sunrise:", data['sys']['sunrise'])
    # print("sunset:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass