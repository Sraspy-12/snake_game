from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"
FONT_SIZE = 24
FONT_TYPE = "normal"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_counter = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score_counter}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))



    def score_increase(self):
        self.score_counter += 1
        self.clear()
        self.update_score()




