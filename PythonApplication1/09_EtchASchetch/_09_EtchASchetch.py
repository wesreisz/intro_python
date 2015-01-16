import turtle
turtle.title("My Etch-a-Sketch")
distance = -1

while distance != "0" :
    color = turtle.textinput("Color", "Enter the pen color (ie blue)")
    angle = turtle.textinput("Angle", "Should I turn (less than -360 to 360)") 
    distance = turtle.textinput("Distance", "Enter turtle distance (maybe 20)")
    direction = turtle.textinput("Direction", "Enter turtle direction (forward or back )") 

    turtle.pencolor(color)
    turtle.right(int(angle))
    
    if "FORWARD" == direction.upper() :
        turtle.forward(int(distance))
    else:
        turtle.backward(int(distance))

