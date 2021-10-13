import requests 

place = input('place name : ').lower()

url = f"https://nominatim.openstreetmap.org/search?q={place}&format=json&limit=1&addressdetails=1&extratags=1&namedetails="

response = requests.get(url)

if response.status_code == 200:
    response = response.json()
    try:
        lat = round(float(response[0]['lat']), 4)
        lon = round(float(response[0]['lon']), 4)
        print(f"latitude   : {str(lat) + '° N' if lat > 0 else str(abs(lat)) + '° S'}")
        print(f"longitude  : {str(lon) + '° E' if lon > 0 else str(abs(lon)) + '° W'}")
        print(f"state      : {response[0]['address']['state']}")
        print(f"country    : {response[0]['address']['country']}")
    except:
        print(f"sorry! no data found for {place.title()}.")
else:
    print(f"sorry! no data found for {place.title()}.")
