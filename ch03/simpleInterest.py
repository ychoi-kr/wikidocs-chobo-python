def simple_interest(p, r, t):
    return int(p * r * t)
    
def simple_interest_amount(p, r, t):
    return int(p * (1 + r * t))

if __name__ == '__main__':
    # Quiz 1
    # ex 1
    print(simple_interest(10000000, 0.03875, 5))
    # ex 2
    print(simple_interest(1100000, 0.05, 5/12))

    # Quiz 2
    # ex 1
    print(simple_interest_amount(10000000, 0.03875, 5))
    # ex 2
    print(simple_interest_amount(1100000, 0.05, 5/12))
