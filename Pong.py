import turtle
import winsound

# World Creation

window = turtle.Screen()
window.title = ("Pong by Momin")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)
score_L = 0
score_R = 0

# Left Paddle Creation

left_p = turtle.Turtle()
left_p.speed(0)
left_p.shape("square")
left_p.color("blue")
left_p.penup()
left_p.goto(-350,0)
left_p.shapesize(stretch_len=1,stretch_wid=5)

#Score

score = turtle.Turtle()
score.speed(0)
score.color("White")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A: 0 Player B: 0", align= 'center', font= ('Courier', 24, "normal"))

# Right Paddle Creation

right_p = turtle.Turtle()
right_p.speed(0)
right_p.shape("square")
right_p.color("red")
right_p.penup()
right_p.goto(350,0)
right_p.shapesize(stretch_len=1,stretch_wid=5)

# Ball Creation

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .45
ball.dy = .45

# Paddle Motion Function

def LeftPadUp():
    y = left_p.ycor()
    y += 40
    left_p.sety(y)
    pass

window.listen()
window.onkeypress(LeftPadUp, "w")

def LeftPadDown():
    y = left_p.ycor()
    y -= 40
    left_p.sety(y)
    pass

window.listen()
window.onkeypress(LeftPadDown, "s")

def RightPadUp():
    y = right_p.ycor()
    y += 40
    right_p.sety(y)
    pass

window.listen()
window.onkeypress(RightPadUp, "Up")

def RightPadDown():
    y = right_p.ycor()
    y -= 40
    right_p.sety(y)
    pass

window.listen()
window.onkeypress(RightPadDown, "Down")

#Auto World Updater

while True:
    window.update()

    #Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Creation
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.Beep(800, 75)

    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.Beep(800, 75)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_L += 1
        score.clear()
        score.write("Player A: {} Player B: {}".format(score_L, score_R), align = "center", font = ("Courier", 24, "normal"))
 
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_R += 1
        score.clear()
        score.write("Player A: {} Player B: {}".format(score_L, score_R), align = "center", font = ("Courier", 24, "normal"))

    #Ball Bouncing Off Paddle
    if ball.xcor() < -340 and ball.ycor() < left_p.ycor() + 50 and ball.ycor() > left_p.ycor() - 50:
        ball.dx *= -1
        winsound.Beep(800, 75)


    if ball.xcor() > 340 and ball.ycor() < right_p.ycor() + 50 and ball.ycor() > right_p.ycor() - 50:
        ball.dx *= -1
        winsound.Beep(800, 75)



