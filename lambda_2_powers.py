def sq(n):
    return lambda x : x**n
s = sq(2)
print(s(int(input("enter any value"))))
