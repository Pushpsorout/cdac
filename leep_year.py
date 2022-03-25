a = int(input ("enter an year to chack it's leep or not"))
year = a%4
if year == 0 :
    year = a%100
    if year == 0:    
        year = a%400
        if year == 0:
           print("it's a leep year")
        else:
            print("it's not a leep year")
    else:
            print("it's a leep year")
else:
            print("it's not a leep year")
