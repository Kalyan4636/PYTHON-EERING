def findContentChildren(g, s):
    i = 0
    j = 0
    g = sorted(g)
    s = sorted(s)

    while i < len(g) and j < len(s):
        i += g[i] <= s[i]
        j = j + 1
    return i

g = [1,2,3]
s = [1,1]
print(findContentChildren(g, s))
