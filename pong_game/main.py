import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball



screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
play_ball = Ball()
l_scoreboard = Scoreboard((-180,240))
r_scoreboard = Scoreboard((180,240))



screen.listen()
screen.onkey(fun= l_paddle.move_up,key= "w")
screen.onkey(fun= l_paddle.move_down,key= "s")
screen.onkey(fun= r_paddle.move_up,key= "Up")
screen.onkey(fun= r_paddle.move_down,key= "Down")

game_is_on = True
while game_is_on:
    time.sleep(play_ball.move_speed)
    play_ball.move_ball()
    if play_ball.ycor()>280 or play_ball.ycor() < -280:
        play_ball.wall_bounce()
    elif play_ball.xcor() <= -340 and play_ball.xcor() > -360 and play_ball.distance(l_paddle) < 50:
        play_ball.paddle_bounce()
        time.sleep(play_ball.move_speed)
    elif play_ball.xcor() >= 340 and play_ball.xcor() < 360 and play_ball.distance(r_paddle) < 50:
        play_ball.paddle_bounce()
        time.sleep(play_ball.move_speed)
    elif play_ball.xcor() > 360:
        l_scoreboard.hold_score()
        screen.update()
        play_ball.reset()
    elif play_ball.xcor() < -360:
        r_scoreboard.hold_score()
        screen.update()
        play_ball.reset()
    screen.update()




















screen.exitonclick()













