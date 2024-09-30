#python program to find roots of quadratic equation
print("U15IG22S0054")
import cmath as m
a=int(input("enter the first cofficient"))
b=int(input("enter the second cofficient"))
c=int(input("enter the third cofficient"))
d=b*b-4*a*c
if d>0:
    root1=-b+m.sqrt(d)/2*a
    root2=-b-m.sqrt(d)/2*a
    print("roots are real")
    print(f"root1={root1} and root2={root2}")
elif d==0:
    root1=root2=-b/2*a
    print("both roots are equal")
    print(f"root1={root1} and root2={root2}")
else:
    real1=-b/1*a
    img1=m.sqrt(d)/2*a
    real2=-b/2*a
    img2=-m.sqrt(d)/2*a
    print("roots are imaginary")
    print(f"root1={real1}+{img1}")
    print(f"root2={real2}+{img2}")