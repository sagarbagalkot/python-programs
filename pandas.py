#write a python program demonstrate data analysis by reading excle file using pandas liabrary
#create a sales data csv file with following colums
#/1.id, 2.product, 3.quantity, 4.price
#/read the csv file into a data frame
#/calculate amount for each product
#/calculate the total sales
#/calculate the average sales per product
#/draw a barchart showing total sale per product 
#/A piechart showing the precentage of total sales per product 
print("U15IG22S0018")
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('salesdata.xlsx')
df['AMT']=df['Qty']*df['Price']
print(df)
total_sales=df['AMT'].sum()
print(f"Total sales amt={total_sales}")
avg_sales_each_product=df.groupby('Product')['AMT'].mean().reset_index()
avg_sales_each_product.columns=['Product','Average Sales']
print(avg_sales_each_product)
total_sales_each_product=df.groupby('Product')['AMT'].sum().reset_index()
total_sales_each_product.columns=['Product','total_sales']
print(total_sales_each_product)
plt.figure(figsize=(10,8))
plt.subplot(2,1,1)
plt.bar(height=total_sales_each_product['total_sales'],x=['A','B'],color=['red','blue'])
plt.legend()
plt.title("REG NO:U15IG22SOO57\n Bar chart showing Total sales for each Product")
plt.xlabel("Product Names")
plt.ylabel("Total sales")
plt.subplot(2,1,2)
plt.pie(total_sales_each_product['total_sales'],labels=['A','B'],autopct='%1.1f%%')
plt.title("REG NO:U15IG22SOO57\n pie chart showing percentage of sales of each product")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
