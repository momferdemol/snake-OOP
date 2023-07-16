from turtle import Turtle

SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Courier", 20, "normal")
SCORE_POSITION = (0, 270)
SCORE_COLOR = "white"


class Scoreboard(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.penup()
        self.color(SCORE_COLOR)
        self.goto(SCORE_POSITION)
        self.write_score()

    def write_score(self):
        """write game score on the canvas."""
        self.clear()
        self.write(f"Score: {self.score}", align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def add_point(self):
        """add new point to game score."""
        self.score += 1
        self.write_score()

    def game_over(self):
        """write game over on canvas."""
        self.goto(0, 0)
        self.write("GAME OVER", align=SCORE_ALIGNMENT, font=SCORE_FONT)
