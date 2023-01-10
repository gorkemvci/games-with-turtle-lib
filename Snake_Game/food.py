from turtle import Turtle
from random import randint , choice

class Food(Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("turtle")
        self.shapesize(1)
        self.penup()     
        self.colors = ["White","Indigo","Blue","Green","Yellow","Orange","Red"] 


    def fooding(self):
        x = randint(-270,270)
        y = randint(-270,270)
        self.color(choice(self.colors))
        self.goto(x,y)
    def clearfooding(self):
        self.clear()
        self.color(choice(self.colors))
        x = randint(-270,270)
        y = randint(-270,270)
        self.goto(x,y)
       
