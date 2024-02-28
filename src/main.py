# import classes
import pygame
import classes.main_menu as mm
import classes.gamemode as gm
import classes.animation as anim
import classes.music as music

# initialize pygame
pygame.init()

# size of window
windowx, windowy = 720, 720
window = pygame.display.set_mode((windowx, windowy))

# FPS of the game
clock = pygame.time.Clock()
FPS = 60

# if true, the game runs
run = True

# initial state of the game
state = 'main_menu'

# holds the temporary state
temp_state = None

# initialization of main menu, VsBot gamemode, and PseudoPvP gamemode
main_menu = mm.MainMenu(windowx, windowy, window)
gamemode_1 = gm.VsBot(windowx, windowy, window)
gamemode_2 = gm.PvP(windowx, windowy, window)

# variables for fade in animation
fadeFrom_isActive = True
fadeFrom = anim.FadeFrom(windowx, windowy)

# sets the cursor to a custom arrow
pygame.mouse.set_cursor(*pygame.cursors.arrow)
mouse_click = True

# loop of the game
while run:
    clock.tick(FPS)
    
    # if state is main_menu, display main menu
    # if state is gm1, display VsBot gamemode
    # if state is gm2, display PvP gamemode
    if state == 'main_menu':
        state = main_menu.display()
    elif state == 'gm1':
        temp_state = gamemode_1.display()
        if temp_state != state:
            main_menu.reset()
            fadeFrom_isActive = True
            gamemode_1.hard_reset()
            state = temp_state
    elif state == 'gm2':
        temp_state = gamemode_2.display()
        if temp_state != state:
            main_menu.reset()
            fadeFrom_isActive = True
            gamemode_2.hard_reset()
            state = temp_state
    elif state == 'quit':
        run = False

    # if true, display fade animation
    if fadeFrom_isActive:
        if fadeFrom.fade(5, window) <= 0:
            fadeFrom.reset()
            main_menu.isActive = True
            fadeFrom_isActive = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # handles global mouse click sound
        if pygame.mouse.get_pressed()[0] and mouse_click == True:
            mouse_click = False
            music.Music.mouse_sound.play()

        if pygame.mouse.get_pressed()[0] == 0:
            mouse_click = True

    pygame.display.update()

pygame.quit()