import turtle

def draw_name():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(100)
    brad.forward(100)
    brad.backward(50)
    brad.right(90)
    brad.forward(150)
    brad.right(180)
    brad.circle(50,-180)
    a = turtle.Turtle()
    a.penup()   
    a.goto(200, 0)
    a.pendown()

    # for i in range(1,4):
    #     brad.right(90)
    #     brad.forward(100)
    # angie = turtle.Turtle()
    # angie.circle(100)
    # angie.shape("circle")
    # angie.color("blue")

    window.exitonclick()
draw_name()
