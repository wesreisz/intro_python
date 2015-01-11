import turtle
turtle.title("My Turtle")

sides = int(turtle.textinput("Title Window", "Enter # of sides"))

for step in range(sides) :
    turtle.forward(50)
    turtle.right(360/sides)
    for smallStep in range(sides) :
        turtle.forward(25)
        turtle.right(360/sides)
