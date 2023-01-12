COLORS = ["Violet","Indigo","Blue","Green","Yellow","Orange","Red"]
from turtle import Turtle
import random 

class CreateCars(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.color(random.choice(COLORS))


    def go_along_way(self,speed):
        new_x = self.xcor() - speed
        self.goto(new_x,self.ycor())   
   



