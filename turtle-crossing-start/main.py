from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
frogger = Player()
screen.listen()
screen.onkey(frogger.move_up, "Up")

cars = []
for _ in range(30):
    car = CarManager()
    cars.append(car)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for car in cars:
        car.move_car()
        # detect turtle hits any car
        if frogger.distance(car) < 15:
            scoreboard.end_game()
            game_is_on = False
    if frogger.ycor() > 290:
        scoreboard.update_score()
        frogger.goto(0, -280)
        for car in cars:
            car.speed_up()

screen.exitonclick()
