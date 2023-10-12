import turtle, random

#window setup
window = turtle.Screen()
window.title("Flap Flap")
window.setup(1000,600)
window.bgcolor("skyblue")
window.tracer(0)


#bird setup
bird = turtle.Turtle()
bird.shape("classic")
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
pipes=[]
def createPipes():
    # pair
    pipe_height = random.randint(1,10)
    # upper pipe
    upperPipe = turtle.Turtle()
    upperPipe.shape("square")
    upperPipe.color("green")
    upperPipe.shapesize(stretch_wid=pipe_height,stretch_len=3)
    upperPipe.penup()
    upperPipe.goto(-500,300)

    

    # lower pipe
    lowerPipe = turtle.Turtle()
    lowerPipe.shape("square")
    lowerPipe.color("green")
    lowerPipe.shapesize(stretch_wid=pipe_height,stretch_len=3)
    lowerPipe.penup()
    lowerPipe.goto(-500,-300)


    pipes.append((upperPipe,lowerPipe))



# gravity factor
gravity = 1
# pipe generating factor
pipeGeneratorFactor = 0
#main game loop: to make the bird fall down
while True:
    #refreshes the screen. the
    # window.update() call is used to make sure that the drawing
    # created by the turtle is displayed on the screen
    window.update()
    bird.sety(bird.ycor() -gravity)
    
    if pipeGeneratorFactor%200 == 0:
        createPipes()

    pipeGeneratorFactor += 1

    # gameend logic
    if bird.ycor() <= -300:
        print("Game Over")
        exit()




#keeps window open util manually closed
turtle.done()
