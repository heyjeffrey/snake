from tkinter import *
from random import randint
from typing import Literal
# from typing import *  # Literal, Any
from PIL import Image, ImageTk
from os import path

movement: Literal[20] = 20
steps_per_sec: Literal[10] = 10
speed: Literal[110] = 1100 // steps_per_sec


class Snake(Canvas):
    def __init__(self) -> None:
        super().__init__(
            width=700,
            height=700,
            background='#53ff1a',
            highlightthickness=0
        )

        self.snake_pos = [(100, 80), (80, 100), (80, 100)]
        self.food_pos = self.set_new_food_pos()
        self.direction: Literal['Right'] = 'Right'

        self.score: Literal[0] = 0

        self.load_img()
        self.create_objects()

        self.bind_all('<Key>', self.on_key_press)

        self.pack()

        self.after(speed, self.perform_actions)

    def load_img(self) -> None:
        try:
            # filename = path.join("D:\Dev\Prj\Python\magics\snake\game.png", "game.png")
            filename = "D:\Dev\Prj\Python\magics\snake\game.png"
            self.snake_body: PhotoImage = ImageTk.PhotoImage(
                Image.open(filename))
            self.food: PhotoImage = ImageTk.PhotoImage(Image.open(filename))
        except IOError as error:
            ws.destroy()
            raise

    def create_objects(self) -> None:
        self.create_text(
            35,
            12,
            text=f'Score: {self.score}',
            tag='score',
            fill='black',
            font=10
        )

        for x_position, y_position in self.snake_pos:
            self.create_image(
                x_position,
                y_position,
                image=self.snake_body,
                tag='snake'
            )

        self.create_image(
            *self.food_pos,
            image=self.food,
            tag='food'
        )

        self.create_rectangle(
            7,
            27,
            690,
            690,
            outline='#d9d8d7'
        )

    def finish_game(self) -> None:
        self.delete(ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f'Game over! You have scored {self.score}!',
            fill='black',
            font=20
        )

    def consume_food(self) -> None:
        if self.snake_pos[0] == self.food_pos:
            self.score += 10
            self.snake_pos.append(self.snake_pos[-1])

            self.create_image(
                *self.snake_pos[-1],
                image=self.snake_body,
                tag='snake'
            )
            self.food_pos: tuple[int, int] = self.set_new_food_pos()
            self.coords(
                self.find_withtag('food'),
                *self.food_pos
            )

            score: tuple[int, ...] = self.find_withtag('score')
            self.itemconfigure(
                score,
                text=f'Score: {self.score}',
                tag='score'
            )

    def boundry(self) -> bool:
        head_x_position, head_y_position = self.snake_pos[0]

        return (
            head_x_position in (0, 700)
            or head_y_position in (20, 700)
            or (head_x_position, head_y_position) in self.snake_pos[1:]
        )

    def snake_movement(self) -> None:
        head_x_position, head_y_position = self.snake_pos[0]

        if self.direction == 'Left':
            new_head_position = (head_x_position - movement, head_y_position)
        elif self.direction == 'Right':
            new_head_position = (head_x_position + movement, head_y_position)
        elif self.direction == 'Down':
            new_head_position = (head_x_position, head_y_position + movement)
        elif self.direction == 'Up':
            new_head_position = (head_x_position, head_y_position - movement)

        self.snake_pos = [new_head_position] + self.snake_pos[:-1]

        for segment, position in zip(self.find_withtag('snake'), self.snake_pos):
            self.coords(segment, position)

    def on_key_press(self, e) -> None:
        new_direction = e.keysym

        all_directions = (
            'Up',
            'Down',
            'Left',
            'Right'
        )
        opposites: tuple[set[str], set[str]] = (
            {'Up', 'Down'},
            {'Left', 'Right'}
        )

        if (
            new_direction in all_directions
            and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction

    def perform_actions(self) -> None:
        if self.boundry():
            self.finish_game()

        self.consume_food()
        self.snake_movement()

        self.after(speed, self.perform_actions)

    def set_new_food_pos(self) -> tuple[int, int]:
        while True:
            x_position: int = randint(1, 29) * movement
            y_position: int = randint(3, 30) * movement
            food_pos: tuple[int, int] = (x_position, y_position)

            if food_pos not in self.snake_pos:
                return food_pos


ws: Tk = Tk()
ws.title('PythonGuides - Snake Game')
ws.resizable(False, False)

board: Snake = Snake()

ws.mainloop()
