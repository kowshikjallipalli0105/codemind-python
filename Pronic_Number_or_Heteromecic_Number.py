x=int(input())
for i in range(1,x+1):
    if i*i+1==x:
        print("NO")
        break
else:
    print("YES")