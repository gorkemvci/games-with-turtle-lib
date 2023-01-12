from turtle import Screen, Turtle, speed
from create_cars import CreateCars 
from player import Player
import random
import time
game_area =Screen()
game_area.tracer(0)
game_area.setup(1400,750)
game_area.bgcolor("royal blue")

start = Turtle()
finish = Turtle()
start.penup()
finish.penup()
start.hideturtle()
finish.hideturtle()
start.goto(0,-345)
finish.goto(0,320)
start.color("medium spring green")
finish.color("deeppink")
start.write("START_____POINT", align="center" , font= ("Arial",30 ,"normal",) )
finish.write("FINISH_____POINT", align="center" , font= ("Arial",30 ,"normal") )
my_turtle = Player()
game_over =Turtle()
game_over.penup()
game_over.hideturtle()
cars_warehouse = []
game_area.listen()
game_area.onkey(my_turtle.cross_move_up,"w")
game_area.onkey(my_turtle.cross_move_down,"s")
game_control = True
level = 1
score_ifblock = 0
scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-540,325)
speed = 10
ifcontrol = 8
while game_control == True:

    if my_turtle.score != score_ifblock:
        score_ifblock = my_turtle.score
        scoreboard.clear() 
    scoreboard.write(f"Level: {level} Score: {my_turtle.score}", align="center", font=('Arial',20,'normal') )

    if random.randint(1,ifcontrol) == 1:
        new_cars = CreateCars()
        new_cars.goto(600,random.randint(-270,270))
        cars_warehouse.append(new_cars)
    for cars in cars_warehouse:
        cars.go_along_way(speed)
        if cars.distance(my_turtle) < 20 :
            game_control= False
            game_over.write("Game OVER...", align="center", font=('Arial',30,'bold') )   
    if finish.distance(my_turtle) < 10 :
            level = level +1
            game_control= False
            speed = speed + 5
            ifcontrol = ifcontrol -1
            game_over.write(f"You will start LEVEL : {level}", align="center", font=('Arial',30,'bold') ) 
            game_area.ontimer(my_turtle.goto(0,-330),2000)
            scoreboard.clear()
            game_over.clear()
            game_control = True
    if start.distance(my_turtle) < 50 :
            game_over.goto(-440,-335)
            game_over.write("The game starts when you get off the START POINT", align="center", font=('Arial',15,'normal') )
    if start.distance(my_turtle) > 50 and start.distance(my_turtle) < 100:
            game_over.goto(0,0)
            game_over.clear()

    time.sleep(0.1)
    game_area.update()

game_area.exitonclick()
