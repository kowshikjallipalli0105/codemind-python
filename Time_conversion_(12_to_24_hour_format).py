from datetime import *
k=input()
k= datetime.strptime(k,'%I:%M %p')
k=str(k)
print(k[11:16])