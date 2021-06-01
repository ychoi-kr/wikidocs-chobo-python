from time import process_time

start = process_time()

n = 2 ** 10
L = L2 = list(range(2, n))

for p in L:
    if p in L2:
        for q in L:
            if (q in L2) and (q!=p and q%p==0):
                L2.remove(q)

end = process_time()

print('elapsed:', end - start)
#print(L2)
