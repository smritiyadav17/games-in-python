""" Pong Game ----- Turtle Module """

# Importing module
import turtle 


# Setup
window = turtle.Screen()
window.title("Pong Game by @Smriti17")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# PaddleA 
# creating a turtle object 
paddleA = turtle.Turtle()
paddleA.speed(0)
# circle, cquare, triangle ,etc.. #bydefault it gets 20x20 pixel
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)


# PaddleB
# creating a turtle object 
paddleB = turtle.Turtle()
paddleB.speed(0)
# circle, cquare, triangle ,etc.. #bydefault it gets 20x20 pixel
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)



# Ball 
ball = turtle.Turtle()
ball.speed(0)
# circle, cquare, triangle ,etc.. #bydefault it gets 20x20 pixel
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
# screen height is 600, so i want score to look at around middle
pen.goto(0,260)



# score 
scoreA = 0 
scoreB = 0 
pen.write(f"Player A: {scoreA}   Player B:{scoreB}", align="center", font=("Courier",24,"normal"))

# Paddle A movement
def paddleA_Up():
	# getting the y cord of paddle A
	y = paddleA.ycor()
	y +=20
	# set value of y to new y(+20)
	paddleA.sety(y)

def paddleA_Down():
	# getting the y cord of paddle A
	y = paddleA.ycor()
	y -=20
	# set value of y to new y(+20)
	paddleA.sety(y)


# Paddle A movement
def paddleB_Up():
	# getting the y cord of paddle A
	y = paddleB.ycor()
	y +=20
	# set value of y to new y(+20)
	paddleB.sety(y)

def paddleB_Down():
	# getting the y cord of paddle A
	y = paddleB.ycor()
	y -=20
	# set value of y to new y(+20)
	paddleB.sety(y)


# Ball Movement
# x movt, y movt 
# every time our ball moves, it moves by 2 pixels
ball.dx = 0.2
ball.dy = -0.2






# keyboard binding
# listen for keyboard input 
window.listen()
# when you press small "w", it wil call paddleA_up func
window.onkeypress(paddleA_Up, "w")
window.onkeypress(paddleA_Down, "s")
window.onkeypress(paddleB_Up, "Up")
window.onkeypress(paddleB_Down, "Down")



# Main Game loop
while True:
	window.update()
	# move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)


	# Border Checking 
	if ball.ycor()>290:
		ball.sety(290)
		ball.dy *= -1

	# Border Checking 
	if ball.ycor()< -290:
		ball.sety(-290)
		ball.dy *= -1


	if ball.xcor() >390:
		ball.goto(0,0)
		ball.dx *= -1
		scoreA += 1
		pen.clear()
		pen.write(f"Player A: {scoreA}   Player B:{scoreB}", align="center", font=("Courier",24,"normal"))



	if ball.xcor()<-390:
		ball.goto(0,0)
		ball.dx *= -1
		scoreB  += 1
		pen.clear()
		pen.write(f"Player A: {scoreA}   Player B:{scoreB}", align="center", font=("Courier",24,"normal"))


	# Paddle Ball collision 
	if (ball.xcor() > 340) and (ball.xcor() < 350) and  (ball.ycor() < paddleB.ycor() +40) and  (ball.ycor() > paddleB.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1

	if (ball.xcor() < -340) and (ball.xcor() > -350) and  (ball.ycor() < paddleA.ycor() +40) and  (ball.ycor() > paddleA.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1



