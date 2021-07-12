import requests, json

url = 'https://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en'
response = requests.get(url)

if response.status_code == 200:       
    response = response.json()
    print(response['quoteText'])
    print(f"~ {response['quoteAuthor']}")
    
else:
    print("Sorry! No quote available.")