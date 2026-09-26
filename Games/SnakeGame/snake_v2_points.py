import pygame
import time
import random

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
green = (100, 255, 110)
red = (255, 0, 0)

screen_width = 630
screen_height = 480
box_size = 30

pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])

# Create the grid
for x in range(0, screen_width, box_size):
    pygame.draw.line(screen, grey, [x, 0], [x, screen_height], 1)
for y in range(0, screen_height, box_size):
    pygame.draw.line(screen, grey, [0, y], [screen_width, y], 1)

snake_size = 3
snake_segments = [[box_size, box_size], [box_size * 2, box_size], [box_size * 3, box_size]]

direction = "right"

# Generate initial food position
food_x = random.randint(0, (screen_width - box_size) // box_size) * box_size
food_y = random.randint(0, (screen_height - box_size) // box_size) * box_size

points = 0

font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    # Move the snake
    head_x = snake_segments[0][0]
    head_y = snake_segments[0][1]

    if direction == "right":
        head_x += box_size
    elif direction == "left":
        head_x -= box_size
    elif direction == "up":
        head_y -= box_size
    elif direction == "down":
        head_y += box_size

    # Check if the snake's head collides with the food
    if head_x == food_x and head_y == food_y:
        # Generate new food position
        food_x = random.randint(0, (screen_width - box_size) // box_size) * box_size
        food_y = random.randint(0, (screen_height - box_size) // box_size) * box_size
        # Extend the snake by adding a new segment
        snake_segments.append([])
        # Increase the points
        points += 1

    # Check if the snake's head touches the end of the grid
    if head_x >= screen_width or head_x < 0 or head_y >= screen_height or head_y < 0:
        running = False

    snake_segments.insert(0, [head_x, head_y])
    snake_segments.pop()

    # Redraw the screen
    screen.fill(black)
    for x in range(0, screen_width, box_size):
        pygame.draw.line(screen, grey, [x, 0], [x, screen_height], 1)
    for y in range(0, screen_height, box_size):
        pygame.draw.line(screen, grey, [0, y], [screen_width, y], 1)
    for segment in snake_segments:
        pygame.draw.rect(screen, green, [segment[0], segment[1], box_size, box_size])

    # Draw the food
    pygame.draw.rect(screen, red, [food_x, food_y, box_size, box_size])

    # Display the points
    points_text = font.render("Points: " + str(points), True, white)
    screen.blit(points_text, (screen_width - 120, 10))

    pygame.display.flip()

    time.sleep(0.09)

pygame.quit()
