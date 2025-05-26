
from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segments(pos)



    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def add_segments(self,pos):
        new_square = Turtle()
        new_square.penup()
        new_square.shape("square")
        new_square.color("white")
        new_square.goto(pos)
        self.segments.append(new_square)

    def extend(self):
        self.add_segments(self.segments[-1].position())




