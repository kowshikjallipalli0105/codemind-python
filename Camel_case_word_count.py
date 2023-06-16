t=input()
if t[0].islower():
    c=1
else:
    c=0
for ch in t:
    if ch.isupper():
        c+=1
print(c)