from turtle import Turtle

class Ball(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("Pink")
        self.penup()
        self.x = 30
        self.y = 30
        self.speed(0)
        self.score_l = 0
        self.score_r = 0

    def ball_starter(self):
        if self.ycor() > 320 :
            self.y = self.y * -1
        if self.ycor() < -320:
            self.y = self.y * -1
        if  self.xcor() > 750:
            self.home()
            self.y = self.y * -1
            self.x = self.x * -1
            self.score_l = self.score_l +1
        if  self.xcor() < -750:
            self.home()
            self.score_r = self.score_r +1
            self.y = self.y * -1
            self.x = self.x * -1

        self.goto(self.xcor() +self.x,self.ycor() + self.y ) 
