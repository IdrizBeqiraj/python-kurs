import seaborn as sns
import pandas as pd
import matplotlib.pyplit as plt

from module1.mian import temperature

my_dataset=pd.read_csv("avgIQpercountry.csv")
my_dataset["Population - 2023"]=my_dataset["Population - 2023"].str.replace(",","").astype(float)

fig=px.scatter_geo(my_dataset,locations="Country",locatinmode="country names", hovername="Country",
                   color="Continent", projection="natural earth",
                   hover_data=["Literacy Rate","Nobel Prices"],color_continues_scale="agsunset",
                   title="Average IQ by Country", template="ploty_dark")
flg.show()