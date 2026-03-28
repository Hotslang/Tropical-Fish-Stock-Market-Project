print import re

def extract_quantity(name):
    name = name.lower()

    if "pair" in name:
        return 2
    if "6 pack" in name or "6ct" in name:
        return 6
    if "10 pack" in name:
        return 10

    return 1


def normalize_listings(listings):
    normalized = []

    for item in listings:
        qty = extract_quantity(item["name"])
        price_per_fish = item["price"] / qty

        normalized.append(price_per_fish)

    return normalized