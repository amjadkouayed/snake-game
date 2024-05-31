from turtle import Turtle

class Scoreboard:
    def __init__(self, ):
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.score = 0
        self.scoreboard.color("white")
        self.scoreboard.setposition(0, 270)
        self.scoreboard.write(f"your score is {self.score}", align= "center", font=('Arial', 15, 'normal'))


    def increase_score(self):
        self.score += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"your score is {self.score}", align= "center", font=('Arial', 15, 'normal'))

    def gameover(self):
        self.scoreboard.setposition(0, 0)
        self.scoreboard.write(f"Game over", align= "center", font=('Arial', 35, 'normal'))