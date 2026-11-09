import turtle
import time
import random

# Game Configuration
DELAY = 0.1
SCORE = 0
HIGH_SCORE = 0

# Screen Setup
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("#1a1a1a")
window.setup(width=600, height=600)
window.tracer(0) 

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#4CAF50")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#FF5252")
food.penup()
food.goto(0, 100)

# Snake Body Segments
segments = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Movement Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main Game Loop
while True:
    window.update()

    # Check for Wall Collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset Score
        SCORE = 0
        pen.clear()
        pen.write(f"Score: {SCORE}  High Score: {HIGH_SCORE}", align="center", font=("Courier", 24, "normal"))

    # Check for Food Collision
    if head.distance(food) < 20:
        # Move food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#81C784")
        new_segment.penup()
        segments.append(new_segment)

        # Increase Score
        SCORE += 1
        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE
        
        pen.clear()
        pen.write(f"Score: {SCORE}  High Score: {HIGH_SCORE}", align="center", font=("Courier", 24, "normal"))

    # Move the body segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head was
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for Head Collisions with Body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()

            SCORE = 0
            pen.clear()
            pen.write(f"Score: {SCORE}  High Score: {HIGH_SCORE}", align="center", font=("Courier", 24, "normal"))

    time.sleep(DELAY)

window.mainloop()
