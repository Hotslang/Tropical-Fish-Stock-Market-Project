print(import requests
from bs4 import BeautifulSoup

def scrape_store(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    listings = []

    for item in soup.select(".product"):  # change per site
        name = item.select_one(".title").text.lower()
        
        if "cory" in name:
            price_text = item.select_one(".price").text.replace("$", "").strip()
            
            try:
                price = float(price_text)
            except:
                continue

            listings.append({
                "name": name,
                "price": price,
                "quantity": 1
            })

    return listings)