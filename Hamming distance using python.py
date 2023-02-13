def hammingDistance(x, y):
    xor = x ^ y
    dist = 0
    while xor:
        dist += 1
        xor &= xor - 1
    return dist

x = 1
y = 4
print(hammingDistance(x, y))
