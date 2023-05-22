def prime(i):
    if i==1:
        return 0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return 0
    else:
        return 1
x=int(input())
for j in range(x):
    k=int(input())
    for l in range(k-1,2,-1):
        if prime(l):
            h=l
            break
    for i in range(k,k+100):
        if prime(i):
            z=i
            break
    if(abs(h-k)<=abs(k-z)):
        print(h)
    else:
        print(z)