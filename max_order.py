L1= [100,200,300,400,500]

for i in range(4):

    a=i
    for j in range(i,5):
        if L1[j]>L1[a]:
            a=j
    temp = L1[i]
    L1[i] = L1[a]
    L1[a] = temp
    
print(L1)
