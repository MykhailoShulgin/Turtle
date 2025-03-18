from turtle import Turtle
from random import random

t = Turtle()
t.speed(200)
for i in range(8000):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()