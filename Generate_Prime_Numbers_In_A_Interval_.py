def prime(j):
    for i in range(2,int(j**0.5+1)):
        if j%i==0:
            return 0
    else:
        return 1
x=int(input())
y=int(input())
k=0
for i in range(x,y+1):
    if prime(i):
        if i==1:
            continue
        print(i)