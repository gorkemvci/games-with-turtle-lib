from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
game_screen = Screen()
game_screen.bgcolor("lightyellow")
game_screen.title("Air Hockey by GoHome Game Inc.")
game_screen.setup(1400,700)
game_screen.tracer(0)
paddles_r = Paddle()
paddles_r.right_left("right")
paddles_r.color("Lightblue")
paddles_l = Paddle()
paddles_l.right_left("left") 
paddles_l.color("Lightgreen")
ball = Ball()
game_screen.listen()
game_screen.onkey(paddles_r.paddle_move_up,"Up")
game_screen.onkey(paddles_r.paddle_move_down,"Down")
game_screen.onkey(paddles_l.paddle_move_up,"w")
game_screen.onkey(paddles_l.paddle_move_down,"s")
game_is_on = True
score = Turtle()
score.penup()
score.goto(0,220)
score.hideturtle()
score_r = 0
score_l = 0
game_screen.update()
while game_is_on == True:
    score.clear() 
    score.write(f"{ball.score_l}  -  {ball.score_r}", align="center" , font= ("Arial",80 ,"normal") )
    game_screen.tracer(0)
    ball.ball_starter()
    if ball.distance(paddles_r.position()) < 50:
        ball.goto(ball.xcor() - 20, ball.ycor())
        ball.x = ball.x * -1
    if ball.distance(paddles_l.position()) < 50 :
        ball.goto(ball.xcor() + 20, ball.ycor())
        ball.x = ball.x * -1  
    
    time.sleep(0.09)    
    game_screen.update()
game_screen.exitonclick()
