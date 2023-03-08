from turtle import Turtle
from typing import Any

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE: int = 20
UP: int = 90
DOWN: int = 270
LEFT: int = 180
RIGHT: int = 0


class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        # segments = []
        self.create_snake()
        self.head: Turtle = self.segments[0]
        # self.move()

    def create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            new_segment: Turtle = Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start=2, stop=0, step=-1
            new_x: float = self.segments[seg_num - 1].xcor()
            # get the position of second last seg
            new_y: float = self.segments[seg_num - 1].ycor()
            # reverse order, let the last seg move to the second last seg position
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
