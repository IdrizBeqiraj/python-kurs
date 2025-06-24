import pandas as pd
import matplotlib.pyplot as plt

#getting data from file
df=pd.read_csv("avgIQpercountry.csv")

avg_iq=df.groupby("Continent")["Average IQ"].mean()

plt.figure(figsize=(10,6))

avg_iq.plot(kind="line", marker="o", color="skyblue")

plt.title("AVG iq by continent")
plt.xlabel("Continent")
plt.ylabel("Average IQ")
plt.show()