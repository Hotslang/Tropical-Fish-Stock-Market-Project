print import numpy as np

def calculate_index(prices):
    if not prices:
        return None

    prices = sorted(prices)

    # remove outliers (top/bottom 10%)
    trim = int(len(prices) * 0.1)
    if len(prices) > 10:
        prices = prices[trim:-trim]

    return round(np.mean(prices), 2)