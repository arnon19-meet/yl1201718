from turtle import*
colormode(225)
import random




class Square(object):
	def __init__ (self,size,shape):
		self.size=size
		self.shape="square"
	def random_color(self):
		self.color=random.randit(0,225)



class Rectangle(object):
	def __init__(self,width,height):
		self.width=width
		self.height=height







