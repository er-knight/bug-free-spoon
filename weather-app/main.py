import requests

api_key = "YOUR API KEY"

city_name = input("city name   : ").lower()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={'metric'}"

response = requests.get(url)

if response.status_code == 200:        
    response = response.json()
    print(f"description : {response['weather'][0]['description']}")
    print(f"temperature : {response['main']['temp']} °C")
    print(f"pressure    : {response['main']['pressure']} hPa")
    print(f"humidity    : {response['main']['humidity']} %")
else:
    print(f"sorry! no data found for {city_name.title()}.")
