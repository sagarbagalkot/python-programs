#fibonaci series
print("U15IG22S0054")
n=int(input("enter the no"))
fib1=0
fib2=1
if fib1==n or fib2==n:
    print(f"{n} belongs to fibonaci series")
else:
    flag=False
    fib3=0
    while fib3<=n:
        fib3=fib1+fib2
        if fib3==n:
            flag=True
            break      
        fib1=fib2
        fib2=fib3
    if flag==True:
        print(f"{n} belongs to fibonaci series")
    else:
        print(f"{n} does not belond to fibonaci series")