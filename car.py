from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10

class Car:
	def __init__(self):
		self.all_cars = []
		self.move_distance=5
		

	def create_car(self,inp):
		random_chance = random.randint(1, 6)
		if random_chance == 1:
			new_car = Turtle()
			new_car.left(90)
			new_car.shape(inp)
			# new_car.color(random.choice(COLORS))
			new_car.penup()
			new_car.speed("fastest")
			new_car.shapesize(stretch_len=2,stretch_wid=1)
			random_y = random.randint(-40, 40)
			new_car.goto(random_y*10,240)
			self.all_cars.append(new_car)

	def move(self):
		for i in self.all_cars:
			i.back(self.move_distance)

	def level_up(self):
		self.move_distance += 5

