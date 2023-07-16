from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SNAKE_SHAPE = "square"
SNAKE_COLOR = "white"
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """create new snake at the start of the game."""
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """build the body of the snake with segments."""
        new_segment = Turtle(shape=SNAKE_SHAPE)
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """add more segments to the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ "move the snake object over the canvas."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """set heading of snake to up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """set heading of snake to down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """set heading of snake to left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """set heading of snake to right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
