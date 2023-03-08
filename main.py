from snake import Snake
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)  # turn off the tracer

snake: Snake = Snake()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # only update when all segs are in right positions
    '''
    time.sleep(0.1)
    snake.move()
    '''
    snake.move()
    time.sleep(0.1)


screen.exitonclick()
