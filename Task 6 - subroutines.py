import turtle
def polygon(sides):
    for count in range (1, sides+1):
        turtle.forward(100)
        turtle.right(360/sides)
polygon(3)
polygon(4)
polygon(5)
