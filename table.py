for i in range (1,11):
    print("\t",i,end='')
print("\n+----------------------------------------------------------------------------------")

for i in range (1,11):
    if i<10:
        print(' ',end='')
    print(i,"| ",end='')
    for j in range(1,11):
        print(i*j,end='\t')
    print()
