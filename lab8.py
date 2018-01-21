# circle=[0,0,1,4,7]
# #0 is x
# #1 is y
# #2 is dx(delta x)
# #3 is dy
# #4 is radius                        
# circle2=[100,100,7,5,8]


from turtle import *
import random
import math

class ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)


# class Reckt(Turtle):
# 	def __init__(self, hight,width,color,speed)
# 	Turtle.__init__(self)
# 	shape=turtle.registershape((0,0),(hight,0),())


ball1=ball(10,"green",1)
ball2=ball(10,"blue",1)


ball1.penup()
ball2.penup()
ball2.goto(100,100)
ball1.goto(-100,-100)
ball2.goto(-231,-100)	
def check_collision(ball1,ball2):
	if(ball_a.shapesize()[0]*10+ball_b.shapesize()[0]*10>=math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+(math.pow(ball_a.ycor()-ball_b.ycor(),2)))):
		    for i in range(10):
			ball1.color("blue")
			ball2.color("green")
			print("boom")
	else:
		print("what a bummer")
			
check_collision(ball2,ball1)

mainloop()