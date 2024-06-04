from turtle import Turtle



STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
FORWARD = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.create_part(position)

    def create_part(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.setpos(position)
        self.snake_parts.append(snake)

    def reset_snake(self):
        for segment in self.snake_parts:
            segment.goto(1200,1200)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]


    def extend(self):
        self.create_part(self.snake_parts[-1].position())



    def move(self):
        for part_num in range(len(self.snake_parts) - 1 , 0, -1): #each part takes the position of the one infront in order to move together
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)

        self.head.forward(FORWARD) # moves the first part forward

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


