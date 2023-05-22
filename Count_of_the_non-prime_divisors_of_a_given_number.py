def prime(j):
    for i in range(2,int(j**0.5+1)):
        if j%i==0:
            return 1
    else:
        return 0
x=int(input())
k=0
for j in range(1,x+1):
    if x%j==0:
        if prime(j):
            k+=1
print(k+1)