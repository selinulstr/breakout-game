from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from ui import UI
import time

screen = Screen()
screen.title("Breakout Game")
screen.setup(width=1600, height=800)
screen.bgcolor("black")
screen.tracer(0)

ui = UI()
ui.header()

score = Scoreboard(lives=5)
paddle = Paddle()
ball = Ball()
bricks = Bricks()

game_is_on = True

screen.listen()
screen.onkey(fun=paddle.move_left, key="Left")
screen.onkey(fun=paddle.move_right, key="Right")


def check_collision_with_walls():
    global ball, game_is_on, score, ui

    if ball.xcor() < -780 or ball.xcor() > 770:
        ball.bounce(x_bounce=True, y_bounce=False)
        return

    if ball.ycor() > 370:
        ball.bounce(x_bounce=False, y_bounce=True)
        return

    if ball.ycor() < -380:
        ball.reset()
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            game_is_on = False
            ui.game_over(win=False)
            return
        ui.change_color()
        return


def check_collision_with_paddle():
    global ball, paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    if ball.distance(paddle) < 110 and ball.ycor() < -350:

        if paddle_x > 0:
            if ball_x > paddle_x:

                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        elif paddle_x < 0:
            if ball_x < paddle_x:

                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


def check_collision_with_bricks():
    global ball, bricks, score

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(4000, 4000)
                bricks.bricks.remove(brick)

            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)

            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    check_collision_with_walls()
    check_collision_with_paddle()
    check_collision_with_bricks()
    if len(bricks.bricks) == 0:
        ui.game_over(win=True)
        break


screen.mainloop()