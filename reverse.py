l = [[1, 2], [3, 4], [5, 6, 7]]
l=l[::-1]
def ters(l):
    for i in range(len(l)):
        (l[i])=(l[i])[::-1]

ters(l)
print(l)

