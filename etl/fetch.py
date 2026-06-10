import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_products(keyword="laptop", page=1):
    url = "https://real-time-amazon-data.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
    }
    params = {
        "query": keyword,
        "page": str(page),
        "country": "IN",
        "sort_by": "RELEVANCE"
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data["data"]["products"]

# Test it
if __name__ == "__main__":
    products = fetch_products("laptop")
    print(f"Fetched {len(products)} products")
    print(products[0])  # print first product to see structure