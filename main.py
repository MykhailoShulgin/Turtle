import turtle
import random

kitty = 6000
kitty += 80

turtle.speed(200)
turtle.color("green")
turtle.shape("turtle")

game = True

idk = random.randint(0, 300)
if game == True:
    while range(idk):
        for i in range(idk):
            turtle.left(idk)
            turtle.forward(idk)
            turtle.left(idk)
            turtle.forward(idk)
            turtle.right(idk)

    

turtle.done()