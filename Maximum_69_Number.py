x=int(input())
a=[]
k=0
while x:
    d=x%10
    x=x//10
    a.append(d)
a=a[::-1]
for i in range(len(a)):
    if a[i] == 6:
        a[i]=9
        break
for i in range(len(a)):
    k=k*10+a[i]
print(k)