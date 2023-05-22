import math
x=int(input())
k=0
s=0
for i in range(x+1,10000):
    t=i
    k=0
    while i:
        d=i%10
        i=i//10
        k=k*10+d
    if(k==t):
        break
for i in range(x-1,1,-1):
    z=i
    s=0
    while i:
        d=i%10
        i=i//10
        s=s*10+d
    if(s==z):
        break
if(abs(x-s)==abs(k-x)):
    print(s,k)
elif(abs(x-s)<abs(k-x)):
    print(s)
else:
    print(k)
        