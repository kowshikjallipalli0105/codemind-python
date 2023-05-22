def prime(x):
    c=0
    for j in range(1,x+1):
        if x%j==0:
            c+=1
    if(c==2):
        return 1
    else:
        return 0
x=int(input())
temp=x
k=prime(x)
n=0
pri=0
if(k==1):
    while temp:
        d=temp%10
        temp=temp//10
        n+=1
        z=prime(d)
        if(z==1):
            pri+=1
    if(n==pri):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
    