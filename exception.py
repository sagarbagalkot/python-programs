#exception handling
print("U15IG22S0054")
try:
    x=int(input("enter the first num"))
    y=int(input("enter the second num"))
    z=x+y
    print(f"the total={z}")
except ValueError:
    print("data is invalied")
finally:
    print("thank you for using our services")