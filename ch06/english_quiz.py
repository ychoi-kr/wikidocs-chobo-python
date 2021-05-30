import random

d = dict()

with open('ko_en.txt') as f:
    for line in f.readlines()[1:]:
        k, v = tuple(line.split('\t'))
        d[k] = v

quiz = list(d.keys())
random.shuffle(quiz)

while True:
    if len(quiz) == 0:
        break
    
    q = quiz.pop()
    print("Write the following sentence in English.")
    print(q)
    a = input("\nyour answer: ")

    if a == d[q].rstrip():
        print('\nresult: Correct!')
    else:
        print("\nresult: Not correct!")
        print("right answer:" + d[q].rstrip() + '\n')

    input()

    print('-' * 80)
