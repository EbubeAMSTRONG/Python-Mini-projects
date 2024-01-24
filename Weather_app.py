import requests

city = input('Lagos')
key = "e60a65bb5d12bbf07d5aa70ba46f422f"
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
response = requests.get(url)
data = response.json

print(f'weather in {city}:{data['weather'][0]['description']}')