#maltiplication table
n=int(input("enter n value"))
for j in range(1,11):
    for i in range(2,n+1):
        x=i*j
        print(x, end=" ")
    print("\n")