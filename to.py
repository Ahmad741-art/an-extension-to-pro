import turtle

def draw_house():
    # Setup the turtle
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    house_turtle = turtle.Turtle()
    house_turtle.speed(5)

    # Draw the base of the house
    house_turtle.penup()
    house_turtle.goto(-100, -100)
    house_turtle.pendown()
    house_turtle.begin_fill()
    house_turtle.color("yellow")
    for _ in range(4):
        house_turtle.forward(200)
        house_turtle.left(90)
    house_turtle.end_fill()

    # Draw the roof
    house_turtle.begin_fill()
    house_turtle.color("red")
    house_turtle.goto(-100, 100)
    house_turtle.goto(0, 200)
    house_turtle.goto(100, 100)
    house_turtle.goto(-100, 100)
    house_turtle.end_fill()

    # Draw the door
    house_turtle.penup()
    house_turtle.goto(-25, -100)
    house_turtle.pendown()
    house_turtle.begin_fill()
    house_turtle.color("brown")
    for _ in range(2):
        house_turtle.forward(50)
        house_turtle.left(90)
        house_turtle.forward(80)
        house_turtle.left(90)
    house_turtle.end_fill()

    # Draw windows
    def draw_window(x, y):
        house_turtle.penup()
        house_turtle.goto(x, y)
        house_turtle.pendown()
        house_turtle.begin_fill()
        house_turtle.color("white")
        for _ in range(4):
            house_turtle.forward(50)
            house_turtle.left(90)
        house_turtle.end_fill()

        # Draw window panes
        house_turtle.color("black")
        house_turtle.penup()
        house_turtle.goto(x, y + 25)
        house_turtle.pendown()
        house_turtle.forward(50)
        house_turtle.penup()
        house_turtle.goto(x + 25, y)
        house_turtle.pendown()
        house_turtle.left(90)
        house_turtle.forward(50)
        house_turtle.right(90)

    # Draw two windows
    draw_window(30, 0)
    draw_window(-80, 0)

    # Draw the chimney
    house_turtle.penup()
    house_turtle.goto(50, 150)
    house_turtle.pendown()
    house_turtle.begin_fill()
    house_turtle.color("gray")
    house_turtle.left(90)
    house_turtle.forward(50)
    house_turtle.right(90)
    house_turtle.forward(30)
    house_turtle.right(90)
    house_turtle.forward(70)
    house_turtle.right(90)
    house_turtle.forward(30)
    house_turtle.right(90)
    house_turtle.forward(20)
    house_turtle.end_fill()

    # Draw grass
    house_turtle.penup()
    house_turtle.goto(-200, -100)
    house_turtle.pendown()
    house_turtle.begin_fill()
    house_turtle.color("green")
    for _ in range(2):
        house_turtle.forward(400)
        house_turtle.right(90)
        house_turtle.forward(50)
        house_turtle.right(90)
    house_turtle.end_fill()

    # Hide the turtle and display the window
    house_turtle.hideturtle()
    turtle.done()

# Call the function to draw the house
draw_house()
