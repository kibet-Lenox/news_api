import requests
import os
from dotenv import load_dotenv

#load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"), override = True)
#load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"), override=True)

load_dotenv(".env", override=True)
api_key = os.getenv("NEWS_API_KEY")
query = "Bomet"

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

response = requests.get(url)
#print(response.json())

if response.status_code == 200:
    data = response.json()
    if data ["totalResults"] == 0:
        print (f"No news for  {query}.")
    else:
        source =data["articles"][0]["source"]["name"]
        reporter = data ["articles"][0]["author"]
        title = data["articles"][0]["title"]
        description =data["articles"][0]["description"]
        date = data ["articles"][0]["publishedAt"]
        content = data["articles"][0]["content"]
    
        print ("="*16)
        print(f"News for {query} town.")
        print ("="*16)
        print(f"\nSource : {source}")
        print(f"\nReporter: {reporter}")
        print(f"\nDescription: {description}.")
        print(f"\nTitle: {title}.")
        print(f"\nDate published: {date}.")
        print(f"\nContent: {content}.")
    
elif response.status_code == 401:
    print("API key is invalid or not yet active. Check your .env file.")

elif response.status_code == 404:
    print(f"City not found: {city}. Check the spelling.")

elif response.status_code == 429:
    print("Too many requests. Wait before trying again.")

else:
    print(f"Unexpected error: {response.status_code}")
    print(response.text)    

