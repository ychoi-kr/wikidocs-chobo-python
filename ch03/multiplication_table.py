def multi(m):
    for n in range(1, 10):
        print(f'{m} * {n} = {m*n:2d}')

if __name__ == '__main__':
    for i in range(2, 10):
        multi(i)
        print()
