import turtle
import random

kitty = 50
kitty += 80

turtle.speed(200)
turtle.color("green")
turtle.shape("turtle")

game = True

idk = random.randint(0, 600)

while range(12):
    for i in range(idk):
        turtle.left(kitty)
        turtle.forward(kitty)
        turtle.left(kitty)

    

turtle.done()