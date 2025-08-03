from turtle import Turtle,Screen
import random

all_turtles=[]
screen=Screen()
screen.setup(width=500,height=400)
user_choice=screen.textinput(title="Make a bet",prompt="which turtle will win the race?")
colors=["red","blue","orange","violet","yellow","green"]
y_positions=[-90,-60,-30,0,30,60]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
screen.update()
if user_choice:
    is_on_race=True
    
while is_on_race:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_on_race=False
            winning_color=turtle.pencolor()
            if user_choice ==winning_color:
                print(f"you've won the bet. the winning turtle is {turtle}")
            else:
                print(f"You've lost. the winning turtle is {turtle}")
   
        
        turtle_speed=random.randint(0,10)
        turtle.forward(turtle_speed)
    
screen.exitonclick()