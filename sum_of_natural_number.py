def num(n):
    if n==0 or n==1:
        return n
    else:
        return(n+num(n-1))

print(num(int(input("enter any number"))))
