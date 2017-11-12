import turtle
turtle.speed(90000001)
turtle.pensize(00.5)

HowManySides=100000
# sideslenght=120
# degree=60
HowManyShapes=361
# angle=20

# for i in range(HowManyShapes):
# 	turtle.left(angle)
# 	for i in range(HowManySides):
# 		turtle.forward(sideslenght)
# 		turtle.left(degree)
a=1
for i in range(HowManyShapes):
	turtle.forward(270)
	turtle.right(50)
	turtle.forward(170)
	turtle.right(100)
	turtle.forward(130)
	turtle.penup()
	turtle.home()
	turtle.right(a)
	turtle.pendown()
	a=a+1

turtle.mainloop()