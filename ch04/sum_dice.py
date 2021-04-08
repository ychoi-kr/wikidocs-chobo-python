dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)

sum_of_the_two_dice = set()

for x in dice1:
    for y in dice2:
        sum_of_the_two_dice.add(x + y)

print(sum_of_the_two_dice)
