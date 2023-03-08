from turtle import _Screen, Screen, Turtle
import time
import random
from typing import Literal


# Step 1:
delay: float = 0.16
score: int = 0
high_score: int = 0


# Step 2:

wn: _Screen = Screen()
wn.title("Snake Game")
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)


head: Turtle = Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food: Turtle = Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments: list[Turtle] = []
pen: Turtle = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:0 High score:0", align="center",
          font=("Courier", 24, "normal"))

# Step 3:


def go_up() -> None:
    if head.direction != "down":
        head.direction = "up"


def go_down() -> None:
    if head.direction != "up":
        head.direction = "down"


def go_left() -> None:
    if head.direction != "right":
        head.direction = "left"


def go_right() -> None:
    if head.direction != "left":
        head.direction = "right"


def move() -> None:
    y = 0.0
    x = 0.0
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y: float = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x: float = head.xcor()
        head.setx(x+20)


# Step 4:
wn.listen()

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_segment: Turtle = Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments)-1, 0, -1):
        x1: float = segments[index-1].xcor()
        y1: float = segments[index-1].ycor()
        segments[index].goto(x1, y1)

    if len(segments) > 0:
        x: float = head.xcor()
        y: float = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {} High score: {}".format(
                score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)
wn.mainloop()
