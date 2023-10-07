import turtle

#window setup
window = turtle.Screen()
window.title("Flap Flap")
window.setup(1000,600,0,0)
window.bgcolor("white")
# window.bgpic(r"C:\Users\akash\aaVS_CODE\PYTHONVScode\Codingal\Additional Projects\Flappy Bird\flapbg.gif") --> working, not necessary now
#----experimenting with importing image using adShaper and register_shape()
window.register_shape(r"C:\Users\akash\aaVS_CODE\PYTHONVScode\Codingal\Additional Projects\Flappy Bird\_bird.gif")
# window.addshape(r"C:\Users\akash\aaVS_CODE\PYTHONVScode\Codingal\Additional Projects\Flappy Bird\_bird.gif") --> both work
print(window.getshapes())
window.tracer(0)


#bird setup
bird = turtle.Turtle()
bird.shape(r"C:\Users\akash\aaVS_CODE\PYTHONVScode\Codingal\Additional Projects\Flappy Bird\_bird.gif")

# bird.shapesize(5,2) --> not working with the gif
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


# create pipes
def createPipes():
    pipes = turtle.Turtle()
    # pair
    # upper pipe
    

    # lower pipe


# gravity factor
gravity = .2
#main game loop: to make the bird fall down
while True:
    #refreshes the screen. the
    # window.update() call is used to make sure that the drawing
    # created by the turtle is displayed on the screen
    window.update()
    bird.sety(bird.ycor() -gravity)



#keeps window open util manually closed
turtle.done()
