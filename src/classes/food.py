import random
from turtle import Turtle

FOOD_COLOR = "red"
FOOD_SPEED = "fastest"
FOOD_SHAPE = "circle"


class Food(Turtle):
    def __init__(
        self, shape: str = FOOD_SHAPE, undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed(FOOD_SPEED)
        self.refresh()

    def refresh(self):
        """place food at new random position on canvas."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
