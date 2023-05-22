x=int(input())
k=str(x)
k=k[::-1]
k=int(k)
c=0
z=0
for i in range(1,x+1):
    if x%i==0:
        c+=1
for i in range(1,k+1):
    if k%i==0:
        z+=1
if z==2 and c==2:
    print("circular prime")
elif ((c==2 and k!=2) or (c!=2 and k==2)) :
    print("prime but not a circular prime")
else:
    print("not prime")