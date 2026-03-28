print from scraper import scrape_store
from normalize import normalize_listings
from index_calc import calculate_index
from database import save_index

# ADD REAL URLs HERE
urls = [
    "https://www.wetspottropicalfish.com/",
    "https://www.aqua-imports.com/"
]

all_listings = []

for url in urls:
    try:
        listings = scrape_store(url)
        all_listings.extend(listings)
    except Exception as e:
        print(f"Error scraping {url}: {e}")

normalized_prices = normalize_listings(all_listings)

index_value = calculate_index(normalized_prices)

print(f"Corydoras Index Today: ${index_value}")

if index_value:
    save_index(index_value)