def compound_interest_amount_withoutN(p, r, t):
    if t == 1:
        return p * (1 + r)
    elif t > 1:
        return compound_interest_amount_withoutN(p, r, t - 1) * (1 + r)


def compound_interest_amount(p, r, t, n):
    if t * n == 1:
        return p * (1 + r / n)
    elif t * n > 1:
        return compound_interest_amount(p, r, t - 1 / n, n) * (1 + r / n)

if __name__ == '__main__':
    print("Quiz 1")
    print("ex 1:", compound_interest_amount_withoutN(3600000, 0.058, 2))
    print("ex 2:", compound_interest_amount_withoutN(10000000, 0.05 / 12, 12))

    print("\nQuiz 2")
    print("ex 1:", compound_interest_amount(1500000, 0.043, 6, 4))
    print("ex 2:", compound_interest_amount(1500000, 0.043, 6, 1/2))
    print("ex 3:", compound_interest_amount(3600000, 0.058, 2, 1))
