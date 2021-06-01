from math import sqrt
from time import process_time

start = process_time()

n = 2 ** 10
N = list(range(2, n))

i = 0
while i <= sqrt(n) and len(N) > i:
    #print('\ncheck multiple of ', N[i])
    j = i
    while i <= j <= n and len(N) > j:
        #print(f'N[{j}]: {N[j]}', end='')
        if N[j] != N[i] and N[j] % N[i] == 0:
            del N[j]
            #print(' <= deleted')
            if len(N) == j:
                break
        else:
            #print('')
            j += 1
    if len(N) == i:
        break
    else:
        i += 1

end = process_time()

print('elapsed:', end - start)
#print('\nprime numbers under', n, ':', N)
