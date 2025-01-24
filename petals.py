import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named rose
rose = turtle.Turtle()
rose.speed(10)
rose.color("red")

# Function to draw a petal
def draw_petal():
    rose.circle(100, 60)
    rose.left(120)
    rose.circle(100, 60)
    rose.left(120)

# Draw the rose
rose.begin_fill()
for _ in range(6):
    draw_petal()
    rose.right(60)
rose.end_fill()

# Hide the turtle and display the window
rose.hideturtle()
turtle.done()