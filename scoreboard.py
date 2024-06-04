from turtle import Turtle

with open("highscore.txt", "r") as file:
    high_score_content = file.read()

class Scoreboard:
    def __init__(self):
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.score = 0
        self.highscore = int(high_score_content)
        self.scoreboard.color("white")
        self.scoreboard.setposition(0, 270)
        self.update_scoreboard()
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.highscore :
            with open("highscore.txt", "w") as file:
                file.write(str(self.score))
            self.highscore = self.score

        self.score = 0 
        self.update_scoreboard()


    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}  |  HighScore: {self.highscore}", align = "center", font =('Arial', 18, 'normal'))




    # def gameover(self):
    #     self.scoreboard.setposition(0, 0)
    #     self.scoreboard.write(f"Game over", align= "center", font=('Arial', 35, 'normal'))