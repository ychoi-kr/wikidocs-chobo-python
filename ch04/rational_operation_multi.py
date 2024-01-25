from functools import reduce

numbers = [int(x) for x in input().split()]

addition = reduce(lambda a, b: a + b, numbers)
subtraction = reduce(lambda a, b: a - b, numbers)
multiplication = reduce(lambda a, b: a * b, numbers)
division = reduce(lambda a, b: a / b, numbers)

print(addition, subtraction, multiplication, division)
