from turtle import Turtle,Screen,textinput

t=Turtle()
screen=Screen()
textinput(None, None)
def forwarded():
    t.forward(10)
    
def backward():
    t.backward(10)

def clockwise():
    new_heading=t.heading()+10
    t.setheading(new_heading)
    
def anticlockwise():
    old_heading=t.heading()-10
    t.setheading(old_heading)
    
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    
screen.listen()
screen.onkey(clockwise,"a")
screen.onkey(backward,"s")
screen.onkey(forwarded,"w")
screen.onkey(anticlockwise,"d")
screen.onkey(clear,"c")
screen.exitonclick()