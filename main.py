import requests

url = "https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey=dffedc695fe8466c8255da9c7b159a3b"

response = requests.get(url)
data = response.json()

print("=== Tech News Today ===\n")

for article in data["articles"][:5]:
    print("Title:", article["title"])
    print("Source:", article["source"]["name"])
    print("Link:", article["url"])
    print("-" * 50)
