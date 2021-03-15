d = int(input())
m = d
b = []

while True:
    d, m = divmod(d, 2)
    b.insert(0, m)
    if d == 0:
        break

print(b)
