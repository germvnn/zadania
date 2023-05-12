import requests
import os
import csv
import argparse

# Konfiguracja zmiennych
api_key = os.getenv('WEATHER_API_PASSWORD')
city = 'Krakow'
country_code = 'PL'
days = '7'
url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/' \
      f'services/timeline/Cracow/next{days}days?unitGroup=metric' \
      f'&key={api_key}&contentType=json'

# Parsowanie argumentów
parser = argparse.ArgumentParser(description='Script to get weather data.')
parser.add_argument('filename', type=str, help='Name of CSV file.')
args = parser.parse_args()

# Import danych
response = requests.get(url)
data = response.json()

# Wywołanie danych określonych w zadaniu
filtered_data = filter(lambda day: day['tempmin'] < 10, data['days'])
results = [{'Data': day['datetime'], 'Temp min': day['tempmin']} for day
           in filtered_data]

# Zapis wyników do pliku CSV
filename = args.filename
if not filename.endswith('.csv'):
    filename += '.csv'
if os.path.exists(filename):
    raise ValueError(f'File {filename} already exists.')
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Data', 'Temp min'])
    writer.writeheader()
    writer.writerows(results)

print(f'The results were saved to a file {filename}.')
