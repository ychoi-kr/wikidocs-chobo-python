y = int(input('What year were you born? '))

k = None
if 1945 < y <= 1964:
    k = input("Are you Korean?(y/n) ").lower()[0] == 'y'

gen = None

if y <= 1924:
    gen = 'the Greatest Generation'
elif y <= 1945 or (y <= 1954 and k):
    gen = 'the Silent Generation'
elif y <= 1963 or (y <= 1964 and not k):
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'a Gen X'
elif y <= 1996:
    gen = 'a millennial'
else:
    gen = 'a Gen Z'

print(f"You're {gen}.")

