x=int(input())
a=0
b=1
for i in range(1,x+1):
   c=a+b
   a=b
   b=c
   if c==x:
       print("True")
       break
else:
    print("False")