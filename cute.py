import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Valentine's Surprise")
screen.setup(width=800, height=600)
screen.tracer(0)  # Disable automatic updates for instant rendering

# Create heart drawer
def draw_heart(t, x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.left(140)
    t.forward(size)
    for _ in range(200):
        t.right(1)
        t.forward(size / 112)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(size / 112)
    t.forward(size)
    t.end_fill()
    t.penup()
    t.setheading(0)

# Create glowing hearts
def draw_glowing_hearts():
    colors = ["#ff4d4d", "#ff6666", "#ff1a1a", "#e60000"]
    hearts = []
    for _ in range(100):
        heart = turtle.Turtle(visible=False)
        heart.speed(0)
        size = random.randint(10, 40)
        x = random.randint(-350, 350)
        y = random.randint(-250, 250)
        color = random.choice(colors)
        hearts.append((heart, x, y, size, color))
    return hearts

def animate_hearts(hearts):
    for heart, x, y, size, color in hearts:
        draw_heart(heart, x, y, size, color)
    screen.update()  # Batch update for instant rendering

# Draw a large main heart
def draw_main_heart():
    main_heart = turtle.Turtle(visible=False)
    main_heart.speed(0)
    draw_heart(main_heart, 0, -50, 112, "red")

# Display message instantly
def display_message():
    message = turtle.Turtle(visible=False)
    message.color("white")
    message.penup()
    message.goto(0, -180)
    message.write("Will you be my Valentine?", align="center", font=("Arial", 28, "bold"))

# Draw roses as detailed shapes
def draw_roses():
    for _ in range(5):
        rose = turtle.Turtle()
        rose.speed(0)
        rose.color("darkred")
        rose.penup()
        rose.shape("triangle")  
        rose.goto(random.randint(-350, 350), random.randint(-250, 250))

# Run the sequence instantly
glowing_hearts = draw_glowing_hearts()
animate_hearts(glowing_hearts)
draw_main_heart()
display_message()
draw_roses()
screen.update()  # Final batch update

turtle.done()
