import requests
import os

api_key = os.getenv('WEATHER_API_PASSWORD')
city = 'Krakow'
country_code = 'PL'
days = '7'
url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/' \
      f'services/timeline/Cracow/next{days}days?unitGroup=metric' \
      f'&key={api_key}&contentType=json'

response = requests.get(url)
data = response.json()

filtered_data = filter(lambda day: day['tempmin'] < 10, data['days'])
list(map(lambda day: print(f"Data {day['datetime']}, "
                           f"TempMin {day['tempmin']}"), filtered_data))