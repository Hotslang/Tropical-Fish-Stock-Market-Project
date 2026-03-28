print import csv
from datetime import date

def save_index(value, filename="data/cory_index.csv"):
    today = date.today()

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, value])