s=input("enter any word")
if len(s)>= 3 :
    if s[-3:]=="ing":
        print(str(s)+"ly")
    else :
        print(str(s)+"ing")
        
