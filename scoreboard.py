from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))
        if self.l_score > 5:
            self.goto(0,0)
            self.write("Left Player: Winner", align="center", font=("Courier", 40, "normal"))
            return False
        elif self.r_score > 5:
            self.goto(0,0)
            self.write("Right Player: Winner", align="center", font=("Courier", 40, "normal"))
            return False
        else:
            return True

    def l_point(self):
        self.l_score += 1
        self.winner = self.update_scoreboard()
        return self.winner


    def r_point(self):
        self.r_score += 1
        self.winner = self.update_scoreboard()
        return self.winner

