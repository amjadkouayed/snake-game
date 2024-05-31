from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        y_location = random.randint(-250, 250)
        x_location = random.randint(-250, 250)
        self.goto(x_location, y_location)