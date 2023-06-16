def reverse(x):
    v= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    x= list(x)
    i, j = 0, len(x) - 1

    while i < j:
        if x[i] in v and x[j] in v:
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1
        elif x[i] in v:
            j -= 1
        else:
            i += 1

    return ''.join(x)

# Example usage
x=input()
r= reverse(x)
print(r)
