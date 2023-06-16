def find_max(x):
    count = 1
    ma = 1

    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            count += 1
        else:
            count = 1

        if count > ma:
            ma = count

    return ma

# Example usage
x=input()
ma = find_max(x)
print(ma)
