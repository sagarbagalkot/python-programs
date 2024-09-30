#python program to implement numpy array operation
print("U15IG22S0054")
import numpy as np
salesdata=np.array([2100,2000,1880,2400,2500,1500,3000,1350,1230,2580,2340,2560,1490,1200])
print("14 days sale are as follows")
for i in range(0,len(salesdata)):
    print(f"day{i+1}={salesdata[i]}")
firstweek=salesdata[0:7]
totalsalesofweek1=np.sum(firstweek)
secondweek=salesdata[7:]
totalsalesofweek2=np.sum(secondweek)
print("first week data is")
for i in range(0,7):
    print(f"day{i+1}={salesdata[i]}")
print("second week data is")
for i in range(7,len(salesdata)):
    print(f"day{i+1}={salesdata[i]}")  
print(f"total sales of first week={totalsalesofweek1}")      
print(f"total sales of second week={totalsalesofweek2}") 
avgsales=np.mean(salesdata)
print(f"Average sales for 14 days={avgsales}")
salesget2000=salesdata[salesdata>2000]
print("the sales data greater than 2000")
print(salesget2000)
print(f"Highest sales data={np.max(salesdata)}")
print(f"lowest sales data={np.min(salesdata)}")    