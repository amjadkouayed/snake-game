from turtle import Turtle

class Scoreboard:
    def __init__(self, ):
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.score = 0
        self.highscore = 0
        self.scoreboard.color("white")
        self.scoreboard.setposition(0, 270)
        self.update_scoreboard()
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
        self.score = 0 
        self.update_scoreboard()


    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}  |  HighScore: {self.highscore}", align = "center", font =('Arial', 18, 'normal'))




    # def gameover(self):
    #     self.scoreboard.setposition(0, 0)
    #     self.scoreboard.write(f"Game over", align= "center", font=('Arial', 35, 'normal'))