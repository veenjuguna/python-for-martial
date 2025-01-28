import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named "love"
love = turtle.Turtle()
love.shape("turtle")
love.color("red")
love.speed(2)

# Function to draw a heart
def draw_heart():
    love.begin_fill()
    love.left(50)
    love.forward(133)
    love.circle(50, 200)
    love.right(140)
    love.circle(50, 200)
    love.forward(133)
    love.end_fill()

# Draw the heart
love.penup()
love.goto(0, -150)
love.pendown()
draw_heart()

# Hide the turtle
love.hideturtle()

# Display a message
love.penup()
love.goto(0, 100)
love.color("black")
love.write("I Love You", align="center", font=("Arial", 24, "bold"))

# Keep the window open
turtle.done()