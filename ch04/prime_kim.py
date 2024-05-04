# written by kim

def prime(n):
    L = list(range(2, n + 1))
    L2 = L[:]

    for p in L:
        if p in L2:
            for q in L:
                if (q in L2) and (q!=p and q%p==0):
                    L2.remove(q)

    print(L2)

if __name__ == '__main__':
    prime(int(input()))
