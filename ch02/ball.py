height = 100
bounce = 3 / 5

i = 1

while i <= 10:
    height = height * bounce
    print(i, round(height, 4))
    i = i + 1
