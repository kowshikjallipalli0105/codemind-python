from datetime import *
k=input()
s = datetime.strptime(k, "%H:%M")
z=s.strftime("%r")[:5]
h=s.strftime("%r")[9:]
print(z,h)