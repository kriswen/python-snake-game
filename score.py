from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()  # hide arrow
        self.penup()  # hide drawing
        self.color("blue")
        self.goto(0, 270)
        self.update_scoreboard()

        # self.write((0, 280), True)
        # self.write(f"Score = {self.score}", True, align="center")

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)





