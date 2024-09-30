#prime number program
print("U15IG22S0054")
n=int(input("enter the no"))
i=2
flag=False
while i<=n//2:
    r=n%i
    if r==0:
        flag=True
        break
    i=i+1
if flag==True:
    print(f"{n} is not a prime no")
else:
    print(f"{n} is a prime no")