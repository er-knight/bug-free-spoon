import requests
import random

url = 'https://type.fit/api/quotes'
response = requests.get(url)

if response.status_code == 200:
    response = response.json()
    quote = response[random.randrange(0, len(response))]
    print(quote['text'])
    print(f"~ {quote['author']}")
    
else:
    print("Sorry! No quote available.")