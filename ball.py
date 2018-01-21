import turtle
from turtle import*
import random
import math

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.r=r
		self.color=color
		self.shape("circle")
		self.shapesize=r/10
		
ball1=Ball(100,200,1,3,30,"green")	

def move(self,screen_width,screen_hight):
	current_x= x.cor()
	current_y= y.cor()

	new_x= current_x+dx
	new_y= current_y+dy

	right_side_ball=new_x+r
	left_side_ball=new_x-r
	upper_side_ball=new_y+r
	lower_side_ball=new_y-r
	self.goto(new_x,new_y)
	ball1.goto(new_x,new_y)

	if (left_side_ball <=(screen_width/2)):
		new_x=current_x
	else:
		new_x= current_x-dx

	if  (right_side_ball>=(screen_width/2)):
		new_x=current_x
	else:
		new_x= current_x+dx

	if (upper_side_ball <=(screen_hight/2)):
		new_y=current_y
	else:
		new_y= current_y+dy

	if (lower_side_ball <=(screen_hight/2)):
		new_y=current_y
	else:
		new_y= current_y-dy

