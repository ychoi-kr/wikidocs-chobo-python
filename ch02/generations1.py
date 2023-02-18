y = int(input('What year were you born? '))

gen = None

if y <= 1924:
    gen = 'the Greatest Generation'
elif y <= 1945:
    gen = 'the Silent Generation'
elif y <= 1964:
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'a Gen X'
elif y <= 1996:
    gen = 'a millennial'
else:
    gen = 'a Gen Z'

print(f"You're {gen}.")

