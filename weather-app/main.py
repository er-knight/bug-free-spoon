import requests

api_key = "YOUR API KEY"

city_name = input("City Name   : ").lower()
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={'metric'}"
response = requests.get(url)

if response.status_code == 200:        
    response = response.json()
    print(f"Description : {response['weather'][0]['description']}")
    print(f"Temperature : {response['main']['temp']} °C")
    print(f"Pressure    : {response['main']['pressure']} hPa")
    print(f"Humidity    : {response['main']['humidity']} %")
else:
    print(f"Sorry! No data found for {city_name.title()}.")