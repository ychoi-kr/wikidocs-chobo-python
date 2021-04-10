def sumOfDigits(num):
    if num >= 1:
        return num % 10 + sumOfDigits(num // 10)
    else:
        return 0

if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))
