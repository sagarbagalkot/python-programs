#python program to demonstrate barchart and line chart using matplot lib
#create 12 months tempreturedata using arrays show the linechart of tempreture over the mohths
#create 4 quaters temprethuredata using arrays 
#show the barchart of doffrent quaters

import numpy as np
import matplotlib.pyplot as plt
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Spe','Oct','Nov','Dec']
temp=np.array([20,15,30,34,35,40,25,29,38,45,39,50])
quarter=['Quarter1','Quarter2','Quarter3','Quarter4']
tempquarter=[25,33,40,28]
plt.figure(figsize=(12,8))
plt.subplot(2,1,1)
plt.plot(months,temp,linestyle='-',color='b',marker='o')
plt.xlabel("Months")
plt.ylabel("Temprature")
plt.title("REG NO:U15IG22SOO54\n Line chart of showing tempreture of 12 months")
plt.legend(months)
plt.subplot(2,1,2)
plt.bar(quarter,tempquarter,color=['red','green','blue','yellow'])
plt.xlabel("Quarters")
plt.ylabel("Temprature Data")
plt.title("REG NO:U15IG22SOO54\n Tempreture Data of four Quarters in year show using barchart")
plt.legend(quarter)
plt.grid(True)
plt.tight_layout()
plt.show()