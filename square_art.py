import turtle
def draw_square(name_square):
    for i in range(0,4):
        name_square.forward(100)
        name_square.right(90)
        

def art():
    window=turtle.Screen()
    window.bgcolor("Red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range (0,37):
        draw_square(brad)
        brad.right(10)
        
    window.exitonclick()

art()
    
