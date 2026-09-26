import pygame
import time
import random

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
green = (100, 255, 110)

screen_width = 630
screen_height = 480
box_size = 30

pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])

# The lines to create the grid
for x in range(0, screen_width, box_size):
    pygame.draw.line(screen, grey, [x, 0], [x, screen_height], 1)
for y in range(0, screen_height, box_size):
    pygame.draw.line(screen, grey, [0, y], [screen_width, y], 1)

snake_size = 3
# This creates the original snake itself with the height, width of the box-size and *2 mean placing the 2 box after it and so on.
snake_segments = [[box_size, box_size], [box_size*2, box_size], [box_size*3, box_size]]

# Initial direction of the snake
direction = "right"

# This loop iterates over each segment in snake_segments. For each segment it calls the pygame.draw.rect() function draws a green rectangle on the screen.
for segment in snake_segments:
    pygame.draw.rect(screen, green, [segment[0], segment[1], box_size, box_size])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change direction based on arrow key presses
            if event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"

    # Move the snake
    # Get the position of the snake's head
    head_x = snake_segments[0][0]
    head_y = snake_segments[0][1]

    # Update the position of the head based on direction
    if direction == "right":
        head_x += box_size
    elif direction == "left":
        head_x -= box_size
    elif direction == "up":
        head_y -= box_size
    elif direction == "down":
        head_y += box_size

    # Insert the new head segment at the beginning of the snake_segments list
    snake_segments.insert(0, [head_x, head_y])

    # Remove the last segment of the snake (the tail)
    snake_segments.pop()

    # Redraw the snake on the screen
    screen.fill(black)
    for x in range(0, screen_width, box_size):
        pygame.draw.line(screen, grey, [x, 0], [x, screen_height], 1)
    for y in range(0, screen_height, box_size):
        pygame.draw.line(screen, grey, [0, y], [screen_width, y], 1)
    for segment in snake_segments:
        pygame.draw.rect(screen, green, [segment[0], segment[1], box_size, box_size])

    pygame.display.flip()

    # Wait for a short time to control the speed of the snake
    time.sleep(0.09)

pygame.quit()
