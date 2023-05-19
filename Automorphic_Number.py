x=int(input())
k=x*x
h=str(x)
h=len(h)
z=0
while k:
    if h==0:
        break
    d=k%10
    k=k//10
    z=z*10+d
    h-=1
z=str(z)
z=z[::-1]
z=int(z)
if z==x:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")