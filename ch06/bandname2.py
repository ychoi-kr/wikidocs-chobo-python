from random import choice

color = open('color.txt').read().split()
food = open('food.txt').read().split()

print(choice(color) + ' ' + choice(food))

