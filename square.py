import turtle
def draw_square():
    brad = turtle.Turtle()
    window=turtle.Screen()
    window.bgcolor("Red")
    brad.shape("turtle")
    brad.color("yellow")
    turtle.speed(2)
    '''turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)'''
    #create square
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    #create circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    #create triangle
    trig = turtle.Turtle()
    trig.color("pink")
    
    trig.left(60)
    trig.forward(100)
    trig.left(120)
    trig.forward(100)
    trig.left(120)
    trig.forward(100)
    window.exitonclick()
draw_square()
    
    
