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



ball1=ball(10,"green",1)
ball2=ball(10,"blue",1)



ball2.goto(-100,1)
ball1.goto(0,1)
	
def check_collision(ball1,ball2):
	if(ball1.radius+ball2.radius <=Math.sqrt(Math.pow(ball1.xcor()-ball2.xcor(),2)+(Math.pow(ball1.ycor()-ball2.ycor(),2)))):
			ball1.color("blue")
			ball2.color("green")
			print("boom")

mainloop()