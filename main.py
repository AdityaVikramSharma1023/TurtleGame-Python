from turtle import Screen
from player import Player
from scoreboard import Score
from car import Car
import time
import os

screen = Screen()
screen.setup(1000,500)
screen.tracer(0)
screen.listen()
screen.bgpic(os.path.join("backgrounds","bg1.png"))

idle = []
walk = []
fire = []

flag = 0
for i in os.listdir("player_walk"):
	screen.register_shape(os.path.join("player_walk",i))
	walk.append((os.path.join("player_walk",i)))

for i in os.listdir("fire"):
	screen.register_shape(os.path.join("fire",i))
	fire.append((os.path.join("fire",i)))

for i in os.listdir("player_idle"):
	screen.register_shape(os.path.join("player_idle",i))
	idle.append((os.path.join("player_idle",i)))


player = Player()
car = Car()
scoreboard = Score()
game_is_on = True


screen.onkeypress(player.up,"Right")
screen.onkeypress(player.down,"Left")


screen.onkeyrelease(player.idle, "Right")
screen.onkeyrelease(player.idle, "Left")



cw = 0
cf = 1
ci = 0
while game_is_on :

	time.sleep(0.1)

	screen.update()
	
	if player.flag == 0:
		player.shape(idle[ci])
	else:
		player.shape(walk[cw])

	car.create_car(fire[0])

	car.move()

	cw = (cw+1) % 10
	cf = (cf+1) % 5
	ci = (ci+1) % 3

	for single_car in car.all_cars:
		single_car.shape(fire[cf])
		if single_car.distance(player) < 20:
			scoreboard.game_over()
			game_is_on = False

	if player.is_at_finish_line():
		player.goto_start()
		car.level_up()
		scoreboard.increase_level()


screen.exitonclick()
