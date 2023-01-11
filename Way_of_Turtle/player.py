from turtle import Turtle

class Player(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        #self.shapesize(2,2)
        self.color("dark violet")
        self.penup()
        self.goto(0,-330)
        self.left(90)
        self.score = 0
    def cross_move_up(self):
            new_y = self.ycor() + 10
            self.goto(self.xcor(),new_y) 
            self.score =self.score + 10      
    def cross_move_down(self):
            new_y = self.ycor() - 10
            self.goto(self.xcor(),new_y)        
            self.score = self.score -30    