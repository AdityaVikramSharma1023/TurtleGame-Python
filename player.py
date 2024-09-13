from turtle import Turtle

STARTING_POSITION = (-450,-160)
MOVE_DISTANCE = 10
FINISH_LINE_X = 450



class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.speed("fastest")
		self.setheading(90)
		self.goto_start()
		self.right(90)
		self.flag = 0
		
	def up (self):
		self.flag = 1
		self.fd(MOVE_DISTANCE)
		

	def down (self):
		self.flag = 1
		self.bk(MOVE_DISTANCE)

	def is_at_finish_line(self):
		if self.xcor() > FINISH_LINE_X:
			return True
		else:
			return False

	def goto_start(self):
		self.goto(STARTING_POSITION)

	def idle(self):
		self.flag = 0
