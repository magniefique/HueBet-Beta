import pygame
import math

# initialize Pygame
pygame.init()

# set the window size
window_size = (400, 400)

# create the window
screen = pygame.display.set_mode(window_size)

# set the clock for controlling the frame rate
clock = pygame.time.Clock()

# define the rectangle
rect = pygame.Rect(0, 0, 50, 50)

# set the initial x position of the rectangle
rect.x = 0

# set the initial y position of the rectangle
rect.y = window_size[1] // 2

# define the speed of the rectangle
speed = 1

# define the frequency of the sine wave
frequency = 0.1

x = 0

max_x = int(math.pi / (2 * frequency)) * 2
print(max_x)

# run the game loop
running = True
while running and x <= max_x:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the x position of the rectangle
    x += speed
    print(x)

    # calculate the y position of the rectangle using sine wave
    rect.y = window_size[1] // 2 - (math.sin(x * frequency) * window_size[1] // 4)

    # fill the screen with white color
    screen.fill((255, 255, 255))

    # draw the rectangle on the screen
    pygame.draw.rect(screen, (255, 0, 0), rect)

    # update the screen
    pygame.display.update()

    # control the frame rate
    clock.tick(60)

# quit Pygame
pygame.quit()