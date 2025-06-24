import pandas as pd
df=pd.read_csv("avgIQpercountry.csv")
print(df.info()) # we see the columns of this dataset
print(df.head()) # we seethe first 5 rows

country_data=df["Country"]
print(country_data)

subset=df[["Country","Average IQ"]]
filtered_DF=subset[subset["Average IQ"]>100]
print(filtered_DF)

#null_mask finding null rows
null_mask=df.isnull()
null_count=null_mask.sum()
print(null_count)

#rwmoving the duplicates
df.drop_duplicates(keep="first",inplace=True)
df["Population - 2023"]=df["Population - 2023"].apply(lambda x: float(x.replace(",","")))

#finding the avg of a continent
avg_iq_per_country=df.groupby('Continent')["Average IQ"].mean()

avg_iq_per_country=avg_iq_per_country.sort_values(ascending=False)
print(avg_iq_per_country)

#calculate nobel prizes by country. and show countries only with more than 1 nobel
# you have to use Group BY, Sum and sort values


nobel_by_country = df.groupby("Country")["Nobel Prices"].sum()
nobel_more_than_one = nobel_by_country[nobel_by_country > 1]
nobel_sorted = nobel_more_than_one.sort_values(ascending=False)
print(nobel_sorted)