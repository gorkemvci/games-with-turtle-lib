from turtle import Turtle, Screen, textinput
import turtle , pandas
my_screen = Screen()
canada_states ="Canada_States/canada_states.gif"
my_screen.title("Canada State Game by Görkem AVCI")
my_screen.setup(600,400)
my_screen.addshape(canada_states)
turtle.shape(canada_states)
state_data = pandas.read_csv("Canada_States/canada_states.csv")
state_name = state_data["states"]
game_count = 0
game_text  = "Welcome to Canada States Game. Please enter a state name"
write_turtle = Turtle()
write_turtle.hideturtle()
write_turtle.penup() 
write_turtle.goto(-240,160)
print(state_name)
while True :
    write_turtle.clear()
    write_turtle.write( game_text , font=('Arial',10,'normal')  )
    user_answer = textinput(title=f"{game_count}/14 Canada States", prompt="Please enter a state name").title()
    for name  in state_name:
        if name  == user_answer:
            state = state_data[state_data.states == user_answer]
            state_turtle = Turtle()
            state_turtle.hideturtle()
            state_turtle.penup() 
            state_turtle.goto(int(state.x), int(state.y))
            state_turtle.write(user_answer)
            game_count = game_count + 1
            game_text = f"Congratulations. You guessed it right, there are {13-game_count} state names left."
            if game_count == 13 :
               game_text = f"Congratulations.You got all the states right.You got all the states right."

            if name  == "Ontario":
                state_turtle = Turtle()
                state_turtle.color("black")
                state_turtle.hideturtle()
                state_turtle.penup() 
                state_turtle.goto(30, -130)
                state_turtle.write("Görkem AVCI", font=('Arial',13,'bold') )
my_screen.exitonclick()
