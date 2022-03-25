def convert(n):
    if n==0 :
        return (n)
    else:
        convert(n//2)
    print(n%2,end='')

convert(int(input("enter any number")))
