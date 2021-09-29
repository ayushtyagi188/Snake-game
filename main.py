from turtle import Turtle,Screen
import time
from s import Snake


s=Screen()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("Snake game")
s.tracer(0)
snake= Snake()
  
game_is_on=True
while game_is_on:
  s.update()
  time.sleep(0.1)
  snake.move() 

s.exitonclick()
