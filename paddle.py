from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        # self.x = x
        # self.y = y

    def create_paddle(self, x, y):
        self.shape('square')
        self.penup()
        self.goto(x, y)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color('white')

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
