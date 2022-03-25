import math
a=int((input("enter the first side of triangle")))
b=int((input("enter the second side of triangle")))
c=int((input("enter the third side of triangle")))
s=(a+b+c)/2
d=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(d)
