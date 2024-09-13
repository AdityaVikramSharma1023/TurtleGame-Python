from turtle import Turtle

class Score(Turtle):

	def __init__(self):
		super().__init__()
		self.level = 1
		self.color('black')
		self.ht()
		self.penup()
		self.update_level()


	def update_level(self):
		self.goto(400,200)
		self.write(f"Level : {self.level}", align="center", font= ("Courier", 20, "normal"))

	def increase_level(self):
		self.level += 1
		self.update_level()		

	def game_over(self):
		self.goto(0,0)
		self.write("Game Over", align="center", font= ("Courier", 24, "normal"))