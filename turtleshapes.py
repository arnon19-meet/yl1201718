import turtle
import random
turtle.speed(600)
turtle.pensize(5)
turtle.register_shape("shape",((0,50),(50,50),(50,0),(25,-50),(0,0)))
# turtle.addshape("shape")
turtle.shape("shape")
HowManySides=5
sideslenght=80
degree=145
HowManyShapes=1
angle=0

colors=["blue,green.red,black,yellow"]
a=0
turtle.pencolor("blue")
turtle.forward(sideslenght)
turtle.left(degree)
turtle.pencolor("blue")
turtle.forward(sideslenght)
turtle.left(degree)
turtle.pencolor("green")
turtle.forward(sideslenght)
turtle.left(degree)
turtle.pencolor("red")
turtle.forward(sideslenght)
turtle.left(degree)
turtle.pencolor("gray")
turtle.forward(sideslenght)
turtle.left(degree)
turtle.pencolor("yellow")
	
turtle.mainloop()