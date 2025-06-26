import seaborn as sns
import pandas as pd
import matplotlib.pyplit as plt

from module1.mian import temperature

my_dataset=pd.read_csv("avgIQpercountry.csv")
my_dataset["Population - 2023"]=my_dataset["Population - 2023"].str.replace(",","").astype(float)

fig=px.scatter_geo(my_dataset,locations="Country",locatinmode="country names", hovername="Country",
                   size="Average IQ", color="Continent", projection="natural earth",
                   title="Average IQ by Country", size_max=20, template="ploty_dark")
flg.show()