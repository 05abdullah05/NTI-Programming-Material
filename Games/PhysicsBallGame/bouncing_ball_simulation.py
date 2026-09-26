# This is a simple bouncing ball simulation using the cmu_graphics library. 
# The ball moves around the window and bounces off the edges. 
# The speed and direction of the ball are controlled by the variables `ballSpeedX` and `ballSpeedY`. 
# The `onAppStart` function initializes the ball's position and speed, while the `moveBall` function updates its position and checks for collisions with the window edges. 
# The `redrawAll` function draws the ball on the screen, and the `onStep` function is called repeatedly to update the ball's position.
from cmu_graphics import *
import random



def onAppStart(app):
    app.ballX = app.width/2
    app.ballY = app.height/2
    app.ballSize = 50
    app.ballSpeedX = 5
    app.ballSpeedY = 3

def moveBall(app):
    app.ballX += app.ballSpeedX
    app.ballY += app.ballSpeedY

    if app.ballX + app.ballSize/2 >= app.width or app.ballX - app.ballSize/2 <= 0:
        app.ballSpeedX = -app.ballSpeedX

    if app.ballY + app.ballSize/2 >= app.height or app.ballY - app.ballSize/2 <= 0:
        app.ballSpeedY = -app.ballSpeedY

def redrawAll(app):
    drawOval(app.ballX - app.ballSize/2, app.ballY - app.ballSize/2,
             app.ballSize, app.ballSize, fill="blue")

def onStep(app):
    moveBall(app)

runApp(width=400, height=400)



