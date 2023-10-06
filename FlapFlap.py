import turtle

#window setup
window = turtle.Screen()
window.title("Flap Flap")
window.setup(1000,600)
window.bgcolor("skyblue")


#bird setup
bird = turtle.Turtle()
# bird.shape()
bird.color("yellow")
bird.goto(-450,200)
bird.penup()

#methods for movement
def flyUp():
    bird.setheading(90)
    bird.forward(50)

def flyDown():
    bird.setheading(270)
    bird.forward(1)
def flyRight():
    bird.setheading(0)
    bird.forward(1)

def flyLeft():
    bird.setheading(180)
    bird.forward(1)
#window control
#invoking event listener so code can listen to keypresses
window.listen()
window.onkeypress(flyUp,"Up")
window.onkeypress(flyDown,"Down")
window.onkeypress(flyRight,"Right")
window.onkeypress(flyLeft,"Left")


# gravity factor
gravity = 1
#main game loop: to make the bird fall down
while True:
    bird.sety(bird.ycor() -gravity)



#keeps window open util manually closed
turtle.done()
