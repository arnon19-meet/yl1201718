import turtle
from turtle import Turtle
import time
import random
import math
from ball import Ball



turtle.tracer(0)
turtle.hideturtle()

RUNNING=True 
SLEEP=0.0077
SCREEN_WIDTH= turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2


NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX =5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY =5
BALLS=[]

MY_BALL = Ball(0,0,0,0,20, ("blue"))

for i in range(NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	if dx== 0:
		dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy== 0:
		dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)		
	color=(random.random(),random.random(),random.random())
	BALL=Ball(x,y,dx,dy,radius,color)
	BALLS.append(BALL)

def move_all_balls():
	for a in BALLS:
		a.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	if(ball_a.radius+ball_b.radius>=math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+(math.pow(ball_a.ycor()-ball_b.ycor(),2)))):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)==True:
				r1=ball_a.radius
				r2=ball_b.radius
				new_x= random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
				new_y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				new_dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				if new_dx== 0:
					new_dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				new_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				if new_dy== 0:	
					new_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				new_radius=random.randint(MINIMUM_BALL_RADIUS,MINIMUM_BALL_RADIUS)		
				new_color=(random.random(),random.random(),random.random())
				if (r1>r2):
					ball_b.goto(new_x,new_y)
					ball_b.dx=new_dx
					ball_b.dy=new_dy
					ball_b.radius=new_radius
					ball_b.color=new_color  
					r1+=1 
				if(r2>r1):
					ball_a.goto(new_x,new_y)
					ball_a.dx=new_dx
					ball_a.dy=new_dy
					ball_a.radius=new_radius
					ball_a.color=new_color 
 					r2+=1
def check_myball_collision():
	for a in BALLS:
		if collide(ball_a,MY_BALL)==True:
			r3=ball.a.radius
			r4=MY_BALL.radius
			new_x= random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
			new_y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			if new_dx== 0:
					new_dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			new_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			if new_dy== 0:
					new_dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
			new_radius=random.randint(MINIMUM_BALL_RADIUS,MINIMUM_BALL_RADIUS)		
			new_color=(random.random(),random.random(),random.random())
			if (r3>r4):
				ball_a.x=new_x
				ball_a.y=new_y
				ball_a.dx=new_dx
				ball_a.dy=new_dy
				ball_a.radius=new_radius
				ball_a.color=new_color 
				r3+=1  
			if(r4>r3):
				MY_BALL.x=new_x
				MY_BALL.y=new_y
				MY_BALL.dx=new_dx
				MY_BALL.dy=new_dy
				MY_BALL.radius=new_radius
				MY_BALL.color=new_color
				r4+=1
def movearound(event):
	MY_BALL.goto(event.x - SCREEN_WIDTH , SCREEN_HEIGHT - event.y)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING:
	if SCREEN_HEIGHT!= turtle.getcanvas().winfo_height()/2 or SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2:
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2 
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	
	move_all_balls()
	check_all_balls_collision()
	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	turtle.getscreen().update()
	time.sleep(SLEEP)
	

turtle.mainloop()