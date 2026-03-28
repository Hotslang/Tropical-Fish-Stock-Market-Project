print import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cory_index.csv", names=["date", "price"])

plt.plot(df["date"], df["price"])
plt.title("Corydoras Price Index")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()