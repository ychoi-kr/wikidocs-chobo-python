from functools import reduce

numbers = []
for x in input().split():
    numbers.append(int(x))

addition = reduce(lambda a, b: a + b, numbers)
subtraction = reduce(lambda a, b: a - b, numbers)
multiplication = reduce(lambda a, b: a * b, numbers)
division = reduce(lambda a, b: a / b, numbers)

print(addition, subtraction, multiplication, division)
