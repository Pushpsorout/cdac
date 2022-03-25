import cmath

a=int(input("enter your first value"))
b=int(input("enter your second value"))
c=int(input("enter your third value"))

sol=(-b-cmath.sqrt(b**2-4*a*c))/2*a
sol2=(-b+cmath.sqrt(b**2-4*a*c))/2*a
print(sol,"\n",sol2)
