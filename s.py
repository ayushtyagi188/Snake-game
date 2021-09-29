from turtle import *
start_pos=[(0,0),(-20,0),(-40,0)]
move_dis=20
class Snake:
  def __init__(self):
     self.y=[]
     self.create_snake()
  
  def create_snake(self):
      for i in start_pos:
        x=Turtle("square")
        x.color('white')
        x.penup()
        x.goto(i)
        self.y.append(x)
  def move(self):
    for j in range(len(self.y)-1,0,-1):
        new_x=self.y[j-1].xcor()
        new_y=self.y[j-1].ycor()
        self.y[j].goto(new_x,new_y)
    self.y[0].forward(move_dis)
                