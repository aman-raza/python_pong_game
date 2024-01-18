from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0

    def move(self):
        x_cor = self.xcor() + self.x_cor
        y_cor = self.ycor() + self.y_cor
        self.goto(x_cor, y_cor)

    def y_bounce(self):
        self.y_cor *= -1

    def x_bounce(self):
        self.x_cor *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()

