n = int(input())
L = list(range(2, n))

for p in L:
    for q in L:
        if q != p and q % p == 0:
            L.remove(q)

print(L)
