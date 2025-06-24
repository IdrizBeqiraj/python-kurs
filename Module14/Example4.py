import pandas as pd
import matplotlib.pyplot as plt

#getting data  from file
df=pd.read_csv("avgIQpercountry.csv")

nobel_prizes=df.groypby("Continent")["Nonel Prices"].sum()

no_of_continents=nobel_prizes.count()

colors=["gold","lightcoral","yellow","thistle","orange","lightskyblue","aquamarie","burlywood"]
plt.figure(figsize=(10,10))

nobel_prizes.plot(kind="pie", colors=colors, autopct="%1.1f%%")

plt.title("Distribution of Nobel Prizes by Countinent")
plt.ylabel("")
plt.tight_layout()
plt.show()