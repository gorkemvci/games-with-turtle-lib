from turtle import Turtle

import random
class SnakeBody(Turtle):
    def __init__(self) :
        super().__init__()
        self.penup()
        self.shape("square")
        self.snake_segment = []
        self.colors = ["White","Indigo","Blue","Green","Yellow","Orange","Red"]
        
    def create_snake(self):
        x_cor = 0
        for _ in range(3):
            my_snake = SnakeBody()
            my_snake.fillcolor(random.choice(self.colors))
            my_snake.goto(x_cor,0)
            self.snake_segment.append(my_snake)
            
    
    def snake_move(self):
            head_position = self.snake_segment[0].position()
            self.snake_segment[0].forward(20)
            for _ in range(len(self.snake_segment)-1):
                n_head_pos = self.snake_segment[_ + 1].position()
                self.snake_segment[_ + 1].goto(head_position)
                head_position = n_head_pos
            
    def nam_nam(self):
        my_snake = SnakeBody()
        my_snake.goto(self.snake_segment[-1].position())
        my_snake.fillcolor(random.choice(self.colors))
        self.snake_segment.append(my_snake)
      
                
            
