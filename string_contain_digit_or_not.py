x=input()
d=[]
c=0

for i in x:
    if i.isdigit():
        d.append(int(i))
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    
    print("Contains",c,"digit")