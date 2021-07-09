from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Sets de la pantalla
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
#Sgte es para eliminar la animación
screen.tracer(0)

#Scoreboard
scoreboard = Scoreboard()

#Sets del juego
paddle_right = Paddle((350,0))
paddle_left = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collition with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collition with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect the goal
    if ball.xcor() > 380:
        scoreboard.l_goal()
        ball.reset()
    elif ball.xcor() < -380:
        scoreboard.r_goal()
        ball.reset()



screen.exitonclick()