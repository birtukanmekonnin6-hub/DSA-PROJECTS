import turtle
import datetime
import math
circle_pen=turtle.Turtle()
hour_hand=turtle.Turtle()
minute_hand=turtle.Turtle()
second_hand=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("white")
screen.setup(width=650,height=650)

def draw_face():
  circle_pen.penup()
  circle_pen.goto(0,-170)
  circle_pen.pendown()
  radius=170
  circle_pen.circle(radius)
  circle_pen.penup()
  circle_pen.goto(0,0)
  circle_pen.left(90)
  circle_pen.forward(radius)
  anglem=90
  for num in range (60,0,-1):
    anglesm=math.radians(anglem)

    x1=170*math.cos(anglesm)
    y1=170*math.sin(anglesm)
    x2=155*math.cos(anglesm)
    y2=155*math.sin(anglesm)
    circle_pen.penup()
    circle_pen.goto(x1,y1)
    circle_pen.pendown()
    circle_pen.goto(x2,y2)
    anglem +=6
  ang=90
  for num in range(12,0,-1):
    circle_pen.pensize(3)
    circle_pen.pencolor("black")
    angl=math.radians(ang)
    x1=170*math.cos(angl)
    y1=170*math.sin(angl)
    x2=140*math.cos(angl)
    y2=140*math.sin(angl)
    circle_pen.penup()
    circle_pen.goto(x1,y1)
    circle_pen.pendown()
    circle_pen.goto(x2,y2)
    ang +=30

  angle=90
  for num in range(12,0,-1):
    angles=math.radians(angle)
    x=130*math.cos(angles)
    y=130*math.sin(angles)
    circle_pen.penup()
    circle_pen.goto(x,y)
    circle_pen.pendown()
    circle_pen.write(num,align="center",font=("arial",17,"bold"))
    angle= angle+30
circle_pen.hideturtle()
draw_face()
screen.register_shape("hour",(
                      (0,-5),
                      (100,-5),
                      (130,0),
                      (100,5),
                      (0,5)))
screen.register_shape("minute",(
                      (0,-3),
                      (80,-3),
                      (140,0),
                      (80,3),
                      (0,3)))
screen.register_shape("second",(
                      (0,-2),
                      (70,-2),
                      (150,0),
                      (70,2),
                      (0,2)))
hour_hand.shape("hour")
minute_hand.shape("minute")
second_hand.shape("second")
hour_hand.penup()
minute_hand.penup()
second_hand.penup()
hour_hand.goto(0,0)
minute_hand.goto(0,0)
second_hand.goto(0,0)
hour_hand.pensize(6)
minute_hand.pensize(4)
second_hand.pensize(2)

hour_hand.color("black")
minute_hand.color("blue")
second_hand.color("red")
screen.tracer(0)
def draw_hand():
  current_time=datetime.datetime.now()
  hour=current_time.hour%12
  minute=current_time.minute
  second=current_time.second
  hour_angle=180-((hour*30)+(minute*0.5)+(second/120))
  minute_angle=180-((minute*6)+(second*0.1))
  second_angle=180-((second*6))
  hour_hand.setheading(hour_angle)
  minute_hand.setheading(minute_angle)
  second_hand.setheading(second_angle)
  screen.update()
  screen.ontimer(draw_hand,1000)
draw_hand()
screen.mainloop()