# Interactive pool-ball physics simulation using CMU Graphics.
# The ball slows from friction and bounces off the table rails.
# Click to reposition the ball; velocity and impulse are displayed above.
import cmu_graphics
from cmu_graphics import *

# Define the ratio of pixels to units of distance
pixels_per_unit = 100

# Global variables for the ball's movement
app.impulse = 0
app.dy = 5
app.dx = 6
# friction factor
app.ff = 0.99



# Draw the pool table
Rect(0,0, 40, 600, fill='burlyWood')
Rect(360,0, 40, 600, fill='burlyWood')
Rect(0,0, 600, 40, fill='burlyWood')
Rect(0,360, 600, 40, fill='burlyWood')

# Draw the middle part of the pool table and the border
border=Rect(0,0,400,400, fill=None, border='black', borderWidth=5)
Rect(40,40, 320, 320, fill='forestGreen')
Rect(40,40,320,320, fill=None, border='black', borderWidth=5)

# Draw the ball
ball = Circle(100, 100, 20, fill='red')

# Define a function to be called when the mouse is clicked
def onMousePress(x, y):
    ball.centerX = x
    ball.centerY = y

# A function to be called every frame
def onStep():
    global pixels_per_unit

    # Calculate the ball's velocity before collision
    v1 = app.dx / pixels_per_unit

    # Apply friction to the ball's velocity
    app.dy = app.dy * app.ff
    app.dx = app.dx * app.ff

    # Change the ball's position based on its velocity
    ball.centerX += app.dx
    ball.centerY += app.dy

    # Check for collisions with the table's borders and update the ball's velocity
    if(ball.centerX >= 340):
        app.dx = -app.dx
    if(ball.centerX <= 60):
        app.dx = -app.dx
    if(ball.centerY >= 340):
        app.dy = -app.dy
        # calculate impulse
        app.impulse = abs(app.dy) / pixels_per_unit * app.ff
    if(ball.centerY <= 60):
        app.dy = -app.dy
        app.impulse = abs(app.dy) / pixels_per_unit * app.ff

    # Impulse and velocity updated values on the screen
    impulseVärde.value = "{:.2f}".format(app.impulse)
    v2 = app.dx / pixels_per_unit
    velocityValueLabel.value = "{:.2f}".format((v2 + v1) / 2)

# Draw the labels for the impulse and velocity values
velocityLabel = Label('Velocity:', 200, 20, fill='black', size=15, font='monospace', bold=True)
velocityValueLabel = Label('', 270, 20, fill='black', size=15, font='monospace', bold=True)
Label('Impulse:', 50, 20, fill='black', size=15, font='monospace', bold=True)
impulseVärde = Label(app.impulse, 110, 20, fill='black', size=15, font='monospace', bold=True)


cmu_graphics.run()
