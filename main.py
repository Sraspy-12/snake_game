import time
from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


my_screen = Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("SNAKE GAME BY SARAS")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()



my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_is_on = True


while game_is_on:

    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_increase()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        score.game_over()

    # DETECT COLLISION WITH TAIL
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10 :
            game_is_on = False
            score.game_over()

my_screen.exitonclick()