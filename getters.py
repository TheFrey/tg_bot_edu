import requests
import json
from Constant import links, TOKEN_WEATHER, MESSAGE
import random
from datetime import datetime
import re


def get_weather(city):
    url = links.format(city=city, token=TOKEN_WEATHER)
    response = requests.get(url=url)
    if response.status_code == 200:
        data = json.loads(response.text)
        temprature = data['main']['temp']
        clouds = data['clouds']['all']
        wind_spd = data['wind']['speed']
        humiditi = data['main']['humidity']
        result = MESSAGE['weather'].format(temprature, clouds, wind_spd, humiditi)
    else:
        result = MESSAGE['error']

    return result


def get_cat_foto_link():
    num = random.randint(0, 37)
    picture = 'catpic/' + str(num) + '.jpg'
    return picture


def get_time():
    date = datetime.now().date()
    time = re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2}', str(datetime.now().time()))
    return MESSAGE['date_time'].format(date, time[0])
