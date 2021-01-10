def compound_interest_amount(p, r, n, t):
    return int(p * (1 + r / n) ** (n * t))

if __name__ == '__main__':
    # ex 1
    print(compound_interest_amount(1500000, 0.043, 4, 6))

    # ex 2
    print(compound_interest_amount(1500000, 0.043, 1/2, 6))
