from turtle import *
import math
from random import randrange


trial = 1000
radius = 100
dots_in_circle = 0


def in_circle(x, y, radius):
    return math.sqrt(x ** 2 + y ** 2) <= radius


def draw_random_dot():
    x, y = randrange(-radius, radius), randrange(-radius, radius)
    goto(x, y)

    global dots_in_circle

    if in_circle(x, y, radius):
        color('red')
        dots_in_circle += 1
    else:
        color('blue')
    dot()


def main():
    shape('turtle')
    
    up(); forward(radius); down(); left(90)
    
    circle(radius)
    
    for i in range(4):
        forward(radius); left(90); forward(radius)
    
    penup()

    global dots_in_circle

    for t in range(trial):
        draw_random_dot()
        print(f'Trial: {t}, Dots in circle: {dots_in_circle}', end='\r')

    pi = 4 * dots_in_circle / trial
    print('\nPi:', pi)


if __name__ == "__main__":
    main()
