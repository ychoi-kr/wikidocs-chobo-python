from math import sqrt

def prime(n):
    N = list(range(2, n + 1))

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

    #print(f'\nprime numbers under {n}: ', end='')
    print(N)

if __name__ == '__main__':
    prime(int(input()))
