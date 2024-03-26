from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')
SCORE_FILE = "data.txt"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(SCORE_FILE) as data:
            self.high_score = int(data.read())
        self.penup()  # hide drawing
        self.hideturtle()
        self.color("blue")
        self.goto(0, 270)
        self.update_scoreboard()

        # self.write((0, 280), True)
        # self.write(f"Score = {self.score}", True, align="center")

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.file_write_high_score()
        self.score = 0
        self.update_scoreboard()

    # Write score to file
    def file_write_high_score(self):
        with open(SCORE_FILE, mode="w") as data:
            data.write(str(f"{self.high_score}"))
