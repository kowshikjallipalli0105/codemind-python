def fun(a):
    i=0
    j=1
    while(1):
        k=i+j
        i=j
        j=k
        if k<a:
            min=k
        if k>a:
            max=k
            break
    if max>a:
        x=max-a
    else:
        x=a-max
    if min>a:
        y=min-a
    else:
        y=a-min
    if x==y:
        print(min,max)
    elif x<y:
        print(max)
    else:
        print(min)
n=int(input())
fun(n)