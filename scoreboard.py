from turtle import Turtle

class Score(Turtle):

	def __init__(self):
		super().__init__()
		self.level = 1
		self.score = 0
		self.color('black')
		self.ht()
		self.penup()
		self.update_level()
		self.update_score()


	def update_level(self):
		level.write(f"Level : {self.level}", align="center", font= ("Courier", 20, "normal"))

	def update_score(self):
		score.write(f"Level : {self.score}", align="center", font= ("Courier", 20, "normal"))


	def increase_level(self):
		self.level += 1
		self.update_level()

	def increase_score(self):
		self.score += 1
		self.update_score()
		

	def game_over(self):
		self.goto(0,0)
		self.write("Game Over", align="center", font= ("Courier", 24, "normal"))