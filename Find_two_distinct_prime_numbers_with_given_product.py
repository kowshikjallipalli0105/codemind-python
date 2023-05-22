x=int(input())
c=0
for i in range(1,x):
    for j in range(i+1,x):
        if i*j==x:
            c+=1
            print(i,j)
            break
if(c==0):
    print("-1")