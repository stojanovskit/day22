from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.listen()
screen.tracer(0)
right_paddle = Paddle()
left_paddle = Paddle()
right_paddle.create_paddle(350, 0)
left_paddle.create_paddle(-350, 0)

ball = Ball()
ball.create_ball()


screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# ball.goto(100,10)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.go_right()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 240:
        ball.bouncex()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -240:
        ball.bouncex()

screen.exitonclick()
