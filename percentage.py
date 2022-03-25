a=int(input("enter the marks of English ="))
b=int(input("enter the marks of Python ="))
c=int(input("enter the marks of Hindi ="))
d=int(input("enter the marks of Math ="))
e=int(input("enter the marks of c++ ="))

percentage = ((a+b+c+d+e)*100)/500

if percentage >= 60 :
    print ("First Division")
elif percentage>=50 and percentage<=59 :
    print ("Second Division")
elif percentage>=40 and percentage<=49 :
    print ("Third Division")
else :
    print ("Fail")
