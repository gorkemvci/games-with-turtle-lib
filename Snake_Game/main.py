from turtle import Screen, Turtle
from snake_body import SnakeBody
from food import Food
import time
my_screen = Screen()
my_screen.tracer(0)
my_screen.setup(width=600,height=600)
my_screen.title("Snake Game by GörkeM AVCI")
my_screen.bgcolor("lightblue")
snake = SnakeBody()
snake.hideturtle()
snake.create_snake()
my_screen.listen()
my_screen.tracer(0)
def up_fun():
    headings =snake.snake_segment[0].heading()
    if headings != 270.0 :
       snake.snake_segment[0].setheading(90)
def down_fun():
    headings =snake.snake_segment[0].heading()
    if headings != 90.0 :
        snake.snake_segment[0].setheading(270)
def east_fun():
    headings =snake.snake_segment[0].heading()
    if headings != 180.0 :
        snake.snake_segment[0].setheading(0)
def west_fun():
    headings =snake.snake_segment[0].heading()
    if headings != 0.0 and 360.0 :
        snake.snake_segment[0].setheading(180)
my_screen.update()
my_screen.onkey(up_fun,"w")
my_screen.onkey(down_fun,"s")
my_screen.onkey(east_fun,"d")
my_screen.onkey(west_fun,"a")

food = Food()
food.fooding()
my_screen.update()
game_over = Turtle()
game_over.hideturtle()
score = Turtle()
score.hideturtle()
score.penup()
score.goto(0,250)
control = True
score_num = 0
while control ==  True :
    my_screen.tracer(0)
    snake.snake_move()
    if food.distance(snake.snake_segment[0]) < 18:
        snake.nam_nam()
        food.clearfooding()
        score_num = score_num+1

        score.clear()
        score.write(f"Score: {score_num}", align="center", font=('Arial',20,'bold') )
    if snake.snake_segment[0].xcor() > 290 or  snake.snake_segment[0].xcor() < -290 or snake.snake_segment[0].ycor() > 290 or  snake.snake_segment[0].ycor() < -290:
        control = False
        game_over.write("Game OVER..", align="center", font=('Arial',30,'bold') )
    for _ in snake.snake_segment:
        if snake.snake_segment[0] !=  _ :
            if snake.snake_segment[0].distance(_) < 10:
                control = False
                game_over.write("Game OVER..", align="center", font=('Arial',30,'bold') )
    my_screen.update() 
    time.sleep(0.1)


my_screen.exitonclick()
