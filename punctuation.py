import string

p = string.punctuation
s = input("enter any string")
for i in s:
    if i in p:
        s = s.replace(i,'')
print(s)

