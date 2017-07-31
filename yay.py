import turtle
#turtle.shape('turtle')
#square=turtle.clone()
#square.shape('square')
#square.goto(100,100)
#square.goto(200,200)
#square.stamp()
#square.goto(100,100)
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"
UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP
def up():
    global direction
    direction = UP
    print("you pressed up!")

turtle.mainloop()
