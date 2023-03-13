import sys
import pygame
import random

pygame.init()
window = pygame.display.set_mode((600, 500))

# initialise dimensions of rectangle
x = 250
y = 250
rect = (x, y, 25,25)

# initialise colours
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# initialise the x and y increments in which the rectangle moves at
x_increment = 5
y_increment = 0

# Generate random co-ordinates for the food to spawn
# Creates a rectangle for the food
food_x = random.randint(0, 600)
food_y = random.randint(0, 500)
print("x = %s \n y= %s" % (food_x, food_y))
food = (food_x, food_y, 25, 25)

# initialise the pygame clock and set fps
clock = pygame.time.Clock()
fps = 60

def move_Up():
    global y_increment, x_increment
    x_increment = 0
    y_increment = -5

def move_Down():
    global y_increment, x_increment
    x_increment = 0
    y_increment = 5


def move_Left():
    global x_increment, y_increment
    y_increment = 0
    x_increment = -5

def move_Right():
    global x_increment, y_increment
    y_increment = 0
    x_increment = 5

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # checks for key presses
        if event.type == pygame.KEYDOWN:

            # Move up
            if event.key == pygame.K_UP:
                move_Up()

            # Move Down
            if event.key == pygame.K_DOWN:
                move_Down()

            # Move Left
            if event.key == pygame.K_LEFT:
                move_Left()

            # Move Right
            if event.key == pygame.K_RIGHT:
                move_Right()

    # Draw snake at every loop
    x += x_increment
    y += y_increment
    window.fill(black)
    rect = pygame.draw.rect(window, green, (x, y, 25, 25))
    food = pygame.draw.rect(window, red, food)
    pygame.display.flip()

    clock.tick(fps)
