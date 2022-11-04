import string
import random


len_alphabet = 10
len_digit = 4
len_special = 1

candidates = list()

for l in range(len_alphabet):
    candidates.append(random.choice(list(set(string.ascii_letters) - set('lIO'))))

for d in range(len_digit):
    candidates.append(random.choice(list(set(string.digits) - set('01'))))

for s in range(len_special):
    candidates.append(random.choice('!@#$%^&*?'))

random.shuffle(candidates)
print(''.join(candidates))
