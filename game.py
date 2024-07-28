import turtle

def mainscreen():
  screen = turtle.Screen()
  screen.title("Pong Game (i cant belive iam doin that fr)")
  screen.bgcolor("black")
  screen.setup(width=800, height=600)
  screen.tracer(0)

def paddles():
    playerone = turtle.Turtle()
    playerone.speed(0)
    playerone.shape("square")
    playerone.color("white")
    playerone.shapesize(stretchWid=5, stretch_en=1)
    playerone.penup()
    playerone.goto(-350, 0)
    playertwo = turtle.Turtle()
    playertwo.speed(0)
    playertwo.shape("square")
    playertwo.color("white")
    playertwo.shapesize(stretchWid=5, stretchLen=1)
    playertwo.penup()
    playertwo.goto(350, 0)
    return playerone, playertwo
def ball():
  ball = turtle.Turtle()
  ball.speed(0)
  ball.shape("square")
  ball.color("white")
  ball.penup()
  ball.goto(0, 0)
  ball.dx = 0.2
  ball.dy = 0.2
  return ball
def main():
    screen = mainscreen()
    playerone, playertwo = paddles()
    ball = ball()
    while True:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        screen.update()
if __name__ == "__main__":
    main()
