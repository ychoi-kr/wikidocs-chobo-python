def simple_interest(p, r, t):
    return round(p * r * t, 2)
    
def simple_interest_amount(p, r, t):
    return round(p * (1 + r * t), 2)

if __name__ == '__main__':
    # ex 1
    print(simple_interest(10000, 0.03875, 5))
    print(simple_interest(1100, 0.05, 5/12))

    # ex 2
    print(simple_interest_amount(10000, 0.03875, 5))
    print(simple_interest_amount(1100, 0.05, 5/12))
