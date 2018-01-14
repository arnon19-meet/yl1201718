# class animal(object):
# 	def __init__(self,sound,name,age,favorite_color):
# 		self.sound=sound
# 		self.name=name
# 		self.age=age		
# 		self.favorite_color=favorite_color
# 	def eat(self,food):
# 		print("Yummy!! " + self.name + " is eating " + food)
# 	def description(self):	
# 		print(self.name + 'is ' +str(self.age)+" years old and loves the color ... ummm... "+self.favorite_color)
# 	def make_sound(self,amount):
# 		print(self.sound*amount)

# aturtle=animal("aaa ", "jeff ", 9001, "idk ")
# aturtle.eat("veggies ")
# aturtle.description()
# aturtle.make_sound(5)


# class person(object):
# 	def __init__(self,name,age,city,gender):
# 		self.name=name
# 		self.age=age
# 		self.city=city
# 		self.gender=gender
# 	def eat(self,food):
# 		print("Yea! it's ya boi " + self.name + "and i am eating " + food)
# 	def team(self,team):
# 		print("i am " + self.name +"from "+team + "and you are watching disney channle ")
# j=person("Jake Poul ", 21 , "England is my city ", "male ")
# j.eat("mr.crab ")
# j.team("team 10 ")
# v=person("Hey Vsauce, Michel here " 27 "where are your fingers " "male")



class song(object):
	def __init__(self, lyrics):
		self.lyrics=lyrics
	def sing_me_a_song(self):		
		print(self.lyrics)
		a=0
		for i in range(len(self.lyrics)):
			print(self.lyrics[a])
			a+=1

r=song([as"roses are red,",
      "violets are blue,",
      "2+2 is 4 ",
      "-1 thats 3"])
r.sing_me_a_song()n
