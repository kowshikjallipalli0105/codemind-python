m=int(input())
for i in range(m):
    n=input()
    d=[]
    c=0
    for i in n:
        if i.isdigit():
            d.append(int(i))
            c+=1
    if c==0:
        print('No')
    else:
        print("Yes")
