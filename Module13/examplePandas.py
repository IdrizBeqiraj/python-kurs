import pandas as pd
produktet=["Apples","Bananas","Oranges","Grapes","Pineapples",]
sales=[150,200,180,90,60]

sales_perProducts=pd.Series(sales,index=produktet)
print(sales_perProducts)

#shitja e rrushit
print(sales_perProducts["Grapes"])

best_selling_products=sales_perProducts.idmax()
print(best_selling_products)