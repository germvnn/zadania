import requests
import argparse
import os

# Utworzenie parsera
parser = argparse.ArgumentParser(description='Script to get weather data')
parser.add_argument('--temp', type=int, help='Minimal temperature value')
args = parser.parse_args()

# Konfiguracja zmiennych
api_key = os.getenv('WEATHER_API_PASSWORD')
city = 'Krakow'
country_code = 'PL'
days = '7'
url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/' \
      f'services/timeline/Cracow/next{days}days?unitGroup=metric' \
      f'&key={api_key}&contentType=json'

# Import danych
response = requests.get(url)
data = response.json()

#
filtered_data = filter(lambda day: day['tempmin'] < args.temp, data['days'])
list(map(lambda day: print(f"Data {day['datetime']}, "
                           f"TempMin {day['tempmin']}"), filtered_data))
