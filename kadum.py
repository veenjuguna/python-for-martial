import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
netflix_turtle = turtle.Turtle()
netflix_turtle.speed(3)
netflix_turtle.color("red")
netflix_turtle.pensize(10)

# Draw the first vertical line
netflix_turtle.penup()
netflix_turtle.goto(-50, -100)
netflix_turtle.pendown()
netflix_turtle.left(90)
netflix_turtle.forward(200)

# Draw the second vertical line
netflix_turtle.penup()
netflix_turtle.goto(50, -100)
netflix_turtle.pendown()
netflix_turtle.forward(200)

# Draw the diagonal line
netflix_turtle.penup()
netflix_turtle.goto(-50, -100)
netflix_turtle.pendown()
netflix_turtle.goto(50, 100)

# Hide the turtle and display the window
netflix_turtle.hideturtle()
turtle.done()