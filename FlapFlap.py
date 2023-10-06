import turtle

#screen setup
window = turtle.Screen()
window.title("Flap Flap")
window.bgcolor("purple")
window.setup(width=1000,height=700)
window.tracer(5)   #

#trying to attach bird image in place of symbol
# window.register_shape("bird","Codingal/Additional Projects/Flappy Bird/_bird.gif")

def flapUp():
    bird.setheading(90)
    bird.forward(10)

def flapDown():
    bird.setheading(270)
    bird.forward(10)

def flapRight():
    bird.setheading(0)
    bird.forward(10)

def flapLeft():
    bird.setheading(180)
    bird.forward(10)

    

#designing bird like object 
bird = turtle.Turtle()
# bird.shape("bird")
bird.color("yellow")
bird.penup()
bird.goto(-250,0)

#window control
# make the window listen for keyboard input.
window.listen()
window.onkeypress(flapUp,"Up")
window.onkeypress(flapDown, "Down")
window.onkeypress(flapRight, "Right")
window.onkeypress(flapLeft, "Left")

# gravity factor
gravity = -0.1

while True:
    #refreshes the screen. the 
    # window.update() call is used to make sure that the drawing
    # created by the turtle is displayed on the screen
    window.update()
    bird.setheading(270)
    bird.sety(bird.ycor() + gravity)    # gravity = -0.1
    bird.setx(bird.xcor() + 0.01)



turtle.done()