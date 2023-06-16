t=input()
d=[]
for i in t:
    if i.isdigit():
        d.append(int(i))
print(sum(d))