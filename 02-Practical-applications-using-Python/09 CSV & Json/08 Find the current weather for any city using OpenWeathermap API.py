import requests, json

# Section 3
api = '747395cfc02c0e89e91d98dd74223139'

# section 1
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

# section 2
city_name = input('Enter city name: ')

# complete url adress
complete_url = base_url + 'q=' + city_name + "&appid=" + api + "&units=metric"

# Response object
response = requests.get(complete_url)

# print(response.text)

x = json.loads(response.text)

if x['cod'] != '404':
    y = x['main']

    corrent_temp = y['temp']
    corrent_pressure = y['pressure']
    corrent_humidity = y['humidity']
    z = x['weather']
    wather_description = z[0]['description']

    print(" Temperature (in metric Unit) = " + str(corrent_temp) +
          '\n Atmospheric Pressure (in metric Unit) = ' + str(corrent_pressure) +
          '\n Humidity (in metric Unit) = ' + str(corrent_humidity) +
          '\n Description = ' + str(wather_description)
          )
else:
    print('City not found')
