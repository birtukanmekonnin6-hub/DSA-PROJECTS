import turtle
import datetime
import math
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

circle_pen=turtle.Turtle()
hour_hand=turtle.Turtle()
minute_hand=turtle.Turtle()
second_hand=turtle.Turtle()
digital_hand=turtle.Turtle()
date_hand=turtle.Turtle()
status_hand=turtle.Turtle()

screen=turtle.Screen()
screen.title("Functional Analog Clock")
screen.bgcolor("#F6F6F6")
screen.setup(width=650,height=650)
FACE_COLOR="#222222"
HOUR_COLOR="#222222"
MINUTE_COLOR="#2878B5"
SECOND_COLOR="#E63946"
BACKGROUND_COLOR="#F6F6F6"



def draw_face():
  circle_pen.penup()
  circle_pen.goto(0,-170)
  circle_pen.pendown()
  radius=170
  circle_pen.pencolor(FACE_COLOR)
  circle_pen.circle(radius)
  circle_pen.penup()
  circle_pen.goto(0,0)
  circle_pen.left(90)
  circle_pen.forward(radius)
  hour_hand.color(HOUR_COLOR)
  minute_hand.color(MINUTE_COLOR)
  second_hand.color(SECOND_COLOR)

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
digital_hand.goto(0,-100)
hour_hand.pensize(6)
minute_hand.pensize(4)
second_hand.pensize(2)

digital_hand.penup()
digital_hand.goto(0, -205)
digital_hand.hideturtle()

date_hand.penup()
date_hand.goto(0, -235)
date_hand.hideturtle()

status_hand.penup()
status_hand.goto(0, -270)
status_hand.hideturtle()
screen.tracer(0)
is_running = True

selected_timezone = None
timezone_name = "Local Time"

timer_version = 0

UPDATE_INTERVAL = 1000

def get_current_time():

    if selected_timezone is None:
        return datetime.datetime.now()

    return datetime.datetime.now(selected_timezone)  
def draw_hand():
  current_time = get_current_time()
  hour=current_time.hour%12
  minute=current_time.minute
  second=current_time.second
  microsecond=current_time.microsecond
  smooth_second=second + microsecond/1000000
  hour_angle=180-((hour*30)+(minute*0.5)+(smooth_second/120))
  minute_angle=180-((minute*6)+(smooth_second*0.1))
  second_angle=180-((smooth_second*6))
  hour_hand.setheading(hour_angle)
  minute_hand.setheading(minute_angle)
  second_hand.setheading(second_angle)

  digital_hand.clear()
  digital_time=current_time.strftime("%I:%M:%S %p")
  digital_hand.write(digital_time,align="center",font=("arial",17,"bold"))
  date_hand.clear()

  current_date = current_time.strftime(
        "%A, %B %d, %Y"
    )
  date_hand.write(
        current_date,
        align="center",
        font=("Arial", 12, "normal")
    )
def display_status():

    status_hand.clear()

    if is_running:
        message = "RUNNING"
    else:
        message = "PAUSED"

    status_hand.write(
        message + " | " + timezone_name,
        align="center",
        font=("Arial", 10, "normal")
    )
def update_clock(version):

      if version != timer_version:
        return

      if not is_running:
        return

      draw_hand()
      display_status()

      screen.update()

      screen.ontimer(
        lambda: update_clock(version),
        UPDATE_INTERVAL
    )
def toggle_pause():

    global is_running
    global timer_version

    is_running = not is_running


    timer_version += 1

    if is_running:
        update_clock(timer_version)

    else:
        display_status()
        screen.update()
def change_timezone():

    global selected_timezone
    global timezone_name
    global timer_version

    choice = screen.textinput(
        "Change Time Zone",
        "Enter time zone:\n\n"
        "Africa/Addis_Ababa\n"
        "Europe/London\n"
        "Asia/Tokyo\n"
        "America/New_York"
    )

    if choice is None:
        return

    try:

        new_timezone = ZoneInfo(choice.strip())

        selected_timezone = new_timezone
        timezone_name = choice.strip()

        timer_version += 1

        if is_running:
            update_clock(timer_version)

        else:
            draw_hand()
            display_status()
            screen.update()

    except (ZoneInfoNotFoundError, ValueError):

        screen.textinput(
            "Invalid Time Zone",
            "Time zone not found. Please try again."
        )
screen.listen()
screen.onkey(toggle_pause, "space")
screen.onkey(change_timezone, "z")
display_status()

update_clock(timer_version)
screen.mainloop()