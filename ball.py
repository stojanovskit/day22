from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_move = 10
        self.x_move = 10

    def create_ball(self):
        self.color("white")
        self.penup()
        self.shape("circle")

    def go_right(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        # self.x_move *= -1

    def bouncex(self):
        # self.y_move *= -1
        self.x_move *= -1
