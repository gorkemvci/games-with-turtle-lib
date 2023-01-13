from turtle import Turtle

class Paddle(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("square")
        self.shapesize(7,1)
        self.penup()

    def right_left(self,position):
        if position == "right":
            self.goto(660,0)
        else: 
            self.goto(-660,0)

    def paddle_move_up(self):
            new_y = self.ycor() + 30
            self.goto(self.xcor(),new_y)        
    def paddle_move_down(self):
            new_y = self.ycor() - 30
            self.goto(self.xcor(),new_y)        



