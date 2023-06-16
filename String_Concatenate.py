a=input()
b=input()
c="".join(sorted(a+b))
c=c.replace('
',"").replace('',"").replace('	',"")
print(c)