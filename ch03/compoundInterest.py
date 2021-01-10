def compound_interest_amount(p, r, t, n):
    return p * (1 + r / n) ** (n * t)

if __name__ == '__main__':
    # ex 1
    print(compound_interest_amount(1500000, 0.043, 6, 4))

    # ex 2
    print(compound_interest_amount(1500000, 0.043, 6, 1/2))
