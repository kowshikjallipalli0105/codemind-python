def prime(i):
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            return 0
    else:
        return 1
def p(i):
    t=i
    k=0
    while i:
        d=i%10
        i=i//10
        k=k*10+d
    if k==t:
        return 1
    else:
        return 0
x=int(input())
for i in range(x+1,100001):
    if i==1:
        continue
    if prime(i):
        if p(i):
            print(i)
            break