import pygame
import math
import random
import classes.button as button
import classes.animation as animation
import classes.delay as dly
import classes.music as music
 
# initialize pygame
pygame.init()

class MainMenuBackground():
    def __init__(self, surfacex:int, surfacey:int):
        # load background image
        self.background = pygame.image.load("assets/imgs/mainmenu/mainmenu_background.png").convert_alpha()
        self.background_scale = surfacex/self.background.get_width(), surfacey/self.background.get_height()
        self.background_resize = pygame.transform.scale(self.background, (self.background.get_width() * self.background_scale[0], self.background.get_height() * self.background_scale[0]))
        self.background_width = self.background_resize.get_height()
        
        self.scroll = 0
        self.tiles = math.ceil(surfacey/self.background_width) + 1

    def display(self, surface:tuple):

        for i in range(0, self.tiles):
            surface.blit(self.background_resize, (0, i * self.background_width + self.scroll))

        self.scroll -= 1

        if abs(self.scroll) > self.background_width:
            self.scroll = 0

class MainMenuTitle():
    
    # color codes for the letters in the title
    white = 255, 255, 255
    red = 255, 68, 68
    green = 69, 255, 58
    blue = 28, 118, 255

    # array containing the colors
    color_array = [red, green, blue]

    def __init__(self, surfacex:int, surfacey:int, scale:float, surface:tuple):
        # initialization of essential values
        self.mainmenu_x, self.mainmenu_y = surfacex, surfacey
        self.mainmenu_scale = scale
            
        # load image for main menu title
        self.mainmenu_img = pygame.image.load("assets/imgs/mainmenu/mainmenu_title.png").convert_alpha()
        
        # animation for main menu image
        self.mainmenu_anim = animation.ResizeAnimation([self.mainmenu_x, self.mainmenu_y, self.mainmenu_img, self.mainmenu_scale], 0)
        
        # initialization for the word "recoloured" for the title animation
        self.mainmenu_font = pygame.font.Font("assets/fonts/Sniglet-ExtraBold.ttf", 44)
        self.mainmenu_text = self.mainmenu_font.render("r e c o l o u r e d", False, (255, 255, 255))
        self.mainmenu_text_resized = pygame.transform.scale(self.mainmenu_text, (int(self.mainmenu_text.get_width() * self.mainmenu_scale), int(self.mainmenu_text.get_height() * self.mainmenu_scale)))
        self.mainmenu_text_resized_rect = self.mainmenu_text_resized.get_rect()
        self.mainmenu_text_resized_rect.topleft = (self.mainmenu_x - (self.mainmenu_text_resized.get_width()/2), ((self.mainmenu_y - (self.mainmenu_img.get_height() * self.mainmenu_scale)/2) + (self.mainmenu_img.get_height() * self.mainmenu_scale)) + (30 * self.mainmenu_scale) - (self.mainmenu_text_resized.get_height()/2))

        # handles color of text
        self.color = (MainMenuTitle.white)

        # renders each individial letter of "recoloured"
        self.mainmenu_space = self.mainmenu_font.render(" ", False, self.color)
        self.mainmenu_r1 = self.mainmenu_font.render("r", False, self.color)
        self.mainmenu_e1 = self.mainmenu_font.render("e", False, self.color)
        self.mainmenu_c = self.mainmenu_font.render("c", False, self.color)
        self.mainmenu_o1 = self.mainmenu_font.render("o", False, self.color)
        self.mainmenu_l = self.mainmenu_font.render("l", False, self.color)
        self.mainmenu_o2 = self.mainmenu_font.render("o", False, self.color)
        self.mainmenu_u = self.mainmenu_font.render("u", False, self.color)
        self.mainmenu_r2 = self.mainmenu_font.render("r", False, self.color)
        self.mainmenu_e2 = self.mainmenu_font.render("e", False, self.color)
        self.mainmenu_d = self.mainmenu_font.render("d", False, self.color)

        # rescales each of the letter 
        self.mainmenu_space_resized = pygame.transform.scale(self.mainmenu_space, (int(self.mainmenu_space.get_width() * self.mainmenu_scale), int(self.mainmenu_space.get_height() * self.mainmenu_scale)))
        self.mainmenu_r1_resized = pygame.transform.scale(self.mainmenu_r1, (int(self.mainmenu_r1.get_width() * self.mainmenu_scale), int(self.mainmenu_r1.get_height() * self.mainmenu_scale)))
        self.mainmenu_e1_resized = pygame.transform.scale(self.mainmenu_e1, (int(self.mainmenu_e1.get_width() * self.mainmenu_scale), int(self.mainmenu_e1.get_height() * self.mainmenu_scale)))
        self.mainmenu_c_resized = pygame.transform.scale(self.mainmenu_c, (int(self.mainmenu_c.get_width() * self.mainmenu_scale), int(self.mainmenu_c.get_height() * self.mainmenu_scale)))
        self.mainmenu_o1_resized = pygame.transform.scale(self.mainmenu_o1, (int(self.mainmenu_o1.get_width() * self.mainmenu_scale), int(self.mainmenu_o1.get_height() * self.mainmenu_scale)))
        self.mainmenu_l_resized = pygame.transform.scale(self.mainmenu_l, (int(self.mainmenu_l.get_width() * self.mainmenu_scale), int(self.mainmenu_l.get_height() * self.mainmenu_scale)))
        self.mainmenu_o2_resized = pygame.transform.scale(self.mainmenu_o2, (int(self.mainmenu_o2.get_width() * self.mainmenu_scale), int(self.mainmenu_o2.get_height() * self.mainmenu_scale)))
        self.mainmenu_u_resized = pygame.transform.scale(self.mainmenu_u, (int(self.mainmenu_u.get_width() * self.mainmenu_scale), int(self.mainmenu_u.get_height() * self.mainmenu_scale)))
        self.mainmenu_r2_resized = pygame.transform.scale(self.mainmenu_r2, (int(self.mainmenu_r2.get_width() * self.mainmenu_scale), int(self.mainmenu_r2.get_height() * self.mainmenu_scale)))
        self.mainmenu_e2_resized = pygame.transform.scale(self.mainmenu_e2, (int(self.mainmenu_e2.get_width() * self.mainmenu_scale), int(self.mainmenu_e2.get_height() * self.mainmenu_scale)))
        self.mainmenu_d_resized = pygame.transform.scale(self.mainmenu_d, (int(self.mainmenu_d.get_width() * self.mainmenu_scale), int(self.mainmenu_d.get_height() * self.mainmenu_scale)))

        # calculates the x position of each letter
        self.mainmenu_letter1 = self.mainmenu_text_resized_rect.x
        self.mainmenu_letter2 = self.mainmenu_letter1 + self.mainmenu_r1_resized.get_width() + (self.mainmenu_space_resized.get_width())
        self.mainmenu_letter3 = self.mainmenu_letter2 + self.mainmenu_e1_resized.get_width() + (self.mainmenu_space_resized.get_width())
        self.mainmenu_letter4 = self.mainmenu_letter3 + self.mainmenu_c_resized.get_width() + (self.mainmenu_space_resized.get_width())
        self.mainmenu_letter5 = self.mainmenu_letter4 + self.mainmenu_o1_resized.get_width() + (self.mainmenu_space_resized.get_width())
        self.mainmenu_letter6 = self.mainmenu_letter5 + self.mainmenu_l_resized.get_width() + (self.mainmenu_space_resized.get_width())
        self.mainmenu_letter7 = self.mainmenu_letter6 + self.mainmenu_o2_resized.get_width() + (self.mainmenu_space_resized.get_width())
        self.mainmenu_letter8 = self.mainmenu_letter7 + self.mainmenu_u_resized.get_width() + (self.mainmenu_space_resized.get_width())
        self.mainmenu_letter9 = self.mainmenu_letter8 + self.mainmenu_r2_resized.get_width() + (self.mainmenu_space_resized.get_width())
        self.mainmenu_letter10 = self.mainmenu_letter9 + self.mainmenu_e2_resized.get_width() + (self.mainmenu_space_resized.get_width())
        self.mainmenu_letter11 = self.mainmenu_letter10 + self.mainmenu_d_resized.get_width() + (self.mainmenu_space_resized.get_width())

        # default y position of the letters
        self.default_letters_y = ((self.mainmenu_y - (self.mainmenu_img.get_height() * self.mainmenu_scale)/2) + (self.mainmenu_img.get_height() * self.mainmenu_scale)) + (30 * self.mainmenu_scale) - (self.mainmenu_r1_resized.get_height()/2)

        # array containing y position of each letter
        self.letters_y = [self.default_letters_y, self.default_letters_y, self.default_letters_y, self.default_letters_y, self.default_letters_y,
                          self.default_letters_y, self.default_letters_y, self.default_letters_y, self.default_letters_y, self.default_letters_y]

        self.letters_y_new = self.default_letters_y - (10 * self.mainmenu_scale)

        # array containing blit function of each letter
        self.mainmenu_letter_blit = [surface.blit(self.mainmenu_r1_resized,(self.mainmenu_letter1, self.letters_y[0])),
                                     surface.blit(self.mainmenu_e1_resized,(self.mainmenu_letter2, self.letters_y[1])),
                                     surface.blit(self.mainmenu_c_resized,(self.mainmenu_letter3, self.letters_y[2])),
                                     surface.blit(self.mainmenu_o1_resized,(self.mainmenu_letter4, self.letters_y[3])),
                                     surface.blit(self.mainmenu_l_resized,(self.mainmenu_letter5, self.letters_y[4])),
                                     surface.blit(self.mainmenu_o2_resized,(self.mainmenu_letter6, self.letters_y[5])),
                                     surface.blit(self.mainmenu_u_resized,(self.mainmenu_letter7, self.letters_y[6])),
                                     surface.blit(self.mainmenu_r2_resized,(self.mainmenu_letter8, self.letters_y[7])),
                                     surface.blit(self.mainmenu_e2_resized,(self.mainmenu_letter9, self.letters_y[8])),
                                     surface.blit(self.mainmenu_d_resized,(self.mainmenu_letter10, self.letters_y[9]))]

        # color of the shadow of the letters
        self.shadow_color = (0, 0, 72)

        # renders the shadow of the letters
        self.mainmenu_r_shadow = self.mainmenu_font.render("r", False, self.shadow_color)
        self.mainmenu_e_shadow = self.mainmenu_font.render("e", False, self.shadow_color)
        self.mainmenu_c_shadow = self.mainmenu_font.render("c", False, self.shadow_color)
        self.mainmenu_o_shadow = self.mainmenu_font.render("o", False, self.shadow_color)
        self.mainmenu_l_shadow = self.mainmenu_font.render("l", False, self.shadow_color)
        self.mainmenu_u_shadow = self.mainmenu_font.render("u", False, self.shadow_color)
        self.mainmenu_d_shadow = self.mainmenu_font.render("d", False, self.shadow_color)

        # rescales the shadows
        self.mainmenu_r_shadow_resized = pygame.transform.scale(self.mainmenu_r_shadow, (self.mainmenu_r1_resized.get_width(), self.mainmenu_r1_resized.get_height()))
        self.mainmenu_e_shadow_resized = pygame.transform.scale(self.mainmenu_e_shadow, (self.mainmenu_e1_resized.get_width(), self.mainmenu_e1_resized.get_height()))
        self.mainmenu_c_shadow_resized = pygame.transform.scale(self.mainmenu_c_shadow, (self.mainmenu_c_resized.get_width(), self.mainmenu_c_resized.get_height()))
        self.mainmenu_o_shadow_resized = pygame.transform.scale(self.mainmenu_o_shadow, (self.mainmenu_o1_resized.get_width(), self.mainmenu_o1_resized.get_height()))
        self.mainmenu_l_shadow_resized = pygame.transform.scale(self.mainmenu_l_shadow, (self.mainmenu_l_resized.get_width(), self.mainmenu_l_resized.get_height()))
        self.mainmenu_u_shadow_resized = pygame.transform.scale(self.mainmenu_u_shadow, (self.mainmenu_u_resized.get_width(), self.mainmenu_u_resized.get_height()))
        self.mainmenu_d_shadow_resized = pygame.transform.scale(self.mainmenu_d_shadow, (self.mainmenu_d_resized.get_width(), self.mainmenu_d_resized.get_height()))
        
        # offset value of the shadows
        self.mainmenu_shadow_offset = int(5 * self.mainmenu_scale)

        # animates the word recoloured
        self.animate = True

        # counter for the animation
        self.counter_1 = 0
        self.delay_anim = dly.Delay()

        # initial state of the animation
        self.state = 'update'

    # displays the title on a surface
    def displayMenu(self, surface:tuple):
        
        # displays and animates the mainmenu image
        self.mainmenu_anim.resize(self.mainmenu_scale, 0.05, 0.05, surface) 

        # blits all letters and their respective shadows
        surface.blit(self.mainmenu_r_shadow_resized,(self.mainmenu_letter1, self.letters_y[0] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_r1_resized,(self.mainmenu_letter1, self.letters_y[0]))
        
        surface.blit(self.mainmenu_e_shadow_resized,(self.mainmenu_letter2, self.letters_y[1] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_e1_resized,(self.mainmenu_letter2, self.letters_y[1]))

        surface.blit(self.mainmenu_c_shadow_resized,(self.mainmenu_letter3, self.letters_y[2] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_c_resized,(self.mainmenu_letter3, self.letters_y[2]))

        surface.blit(self.mainmenu_o_shadow_resized,(self.mainmenu_letter4, self.letters_y[3] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_o1_resized,(self.mainmenu_letter4, self.letters_y[3]))

        surface.blit(self.mainmenu_l_shadow_resized,(self.mainmenu_letter5, self.letters_y[4] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_l_resized,(self.mainmenu_letter5, self.letters_y[4]))

        surface.blit(self.mainmenu_o_shadow_resized,(self.mainmenu_letter6, self.letters_y[5] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_o2_resized,(self.mainmenu_letter6, self.letters_y[5]))

        surface.blit(self.mainmenu_u_shadow_resized,(self.mainmenu_letter7, self.letters_y[6] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_u_resized,(self.mainmenu_letter7, self.letters_y[6]))

        surface.blit(self.mainmenu_r_shadow_resized,(self.mainmenu_letter8, self.letters_y[7] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_r2_resized,(self.mainmenu_letter8, self.letters_y[7]))

        surface.blit(self.mainmenu_e_shadow_resized,(self.mainmenu_letter9, self.letters_y[8] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_e2_resized,(self.mainmenu_letter9, self.letters_y[8]))

        surface.blit(self.mainmenu_d_shadow_resized,(self.mainmenu_letter10, self.letters_y[9] + self.mainmenu_shadow_offset))
        surface.blit(self.mainmenu_d_resized,(self.mainmenu_letter10, self.letters_y[9]))

        # responsible of animating the word "recoloured"
        self.animateMenu(self.animate, surface)

    # animates the word "recoloured"
    def animateMenu(self, isActivated:bool, surface:tuple):
        if isActivated:
            if self.counter_1 < len(self.letters_y):
                """
                STATES:
                update = change the y value of the letter and change its color\n
                delay = delays the animation for each letter\n
                reset = changes the y value of the letter back to its original y value and changes its color to the default color 
                """
                if self.state == 'update':
                    self.letters_y[self.counter_1] = self.letters_y_new
                    self.color = (MainMenuTitle.color_array[(random.randint(0,2))])
                    self.updateMenu('update', self.counter_1)
                    self.state = 'delay'
                if self.state == 'delay':
                    if self.delay_anim.delay(1, 12):
                        self.delay_anim.reset()
                        self.state = 'reset'
                if self.state == 'reset':
                    self.letters_y[self.counter_1] = self.default_letters_y
                    self.color = (MainMenuTitle.white)
                    self.updateMenu('update', self.counter_1)
                    self.counter_1 += 1
                    self.state = 'update'
            else:
                self.counter_1 = 0
    
    # updates and reblits each letter
    def updateMenu(self, state:str, counter:int):
        if state == 'update':
            if counter == 0:
                self.mainmenu_r1 = self.mainmenu_font.render("r", False, self.color)
                self.mainmenu_r1_resized = pygame.transform.scale(self.mainmenu_r1, (int(self.mainmenu_r1.get_width() * self.mainmenu_scale), int(self.mainmenu_r1.get_height() * self.mainmenu_scale)))
            elif counter == 1:
                self.mainmenu_e1 = self.mainmenu_font.render("e", False, self.color)
                self.mainmenu_e1_resized = pygame.transform.scale(self.mainmenu_e1, (int(self.mainmenu_e1.get_width() * self.mainmenu_scale), int(self.mainmenu_e1.get_height() * self.mainmenu_scale)))
            elif counter == 2:
                self.mainmenu_c = self.mainmenu_font.render("c", False, self.color)
                self.mainmenu_c_resized = pygame.transform.scale(self.mainmenu_c, (int(self.mainmenu_c.get_width() * self.mainmenu_scale), int(self.mainmenu_c.get_height() * self.mainmenu_scale)))
        
            elif counter == 3:
                self.mainmenu_o1 = self.mainmenu_font.render("o", False, self.color)
                self.mainmenu_o1_resized = pygame.transform.scale(self.mainmenu_o1, (int(self.mainmenu_o1.get_width() * self.mainmenu_scale), int(self.mainmenu_o1.get_height() * self.mainmenu_scale)))
        
            elif counter == 4:
                self.mainmenu_l = self.mainmenu_font.render("l", False, self.color)
                self.mainmenu_l_resized = pygame.transform.scale(self.mainmenu_l, (int(self.mainmenu_l.get_width() * self.mainmenu_scale), int(self.mainmenu_l.get_height() * self.mainmenu_scale)))
        
            elif counter == 5:
                self.mainmenu_o2 = self.mainmenu_font.render("o", False, self.color)
                self.mainmenu_o2_resized = pygame.transform.scale(self.mainmenu_o2, (int(self.mainmenu_o2.get_width() * self.mainmenu_scale), int(self.mainmenu_o2.get_height() * self.mainmenu_scale)))
        
            elif counter == 6:
                self.mainmenu_u = self.mainmenu_font.render("u", False, self.color)
                self.mainmenu_u_resized = pygame.transform.scale(self.mainmenu_u, (int(self.mainmenu_u.get_width() * self.mainmenu_scale), int(self.mainmenu_u.get_height() * self.mainmenu_scale)))
        
            elif counter == 7:
                self.mainmenu_r2 = self.mainmenu_font.render("r", False, self.color)
                self.mainmenu_r2_resized = pygame.transform.scale(self.mainmenu_r2, (int(self.mainmenu_r2.get_width() * self.mainmenu_scale), int(self.mainmenu_r2.get_height() * self.mainmenu_scale)))
       
            elif counter == 8:
                self.mainmenu_e2 = self.mainmenu_font.render("e", False, self.color)
                self.mainmenu_e2_resized = pygame.transform.scale(self.mainmenu_e2, (int(self.mainmenu_e2.get_width() * self.mainmenu_scale), int(self.mainmenu_e2.get_height() * self.mainmenu_scale)))
       
            elif counter == 9:
                self.mainmenu_d = self.mainmenu_font.render("d", False, self.color)
                self.mainmenu_d_resized = pygame.transform.scale(self.mainmenu_d, (int(self.mainmenu_d.get_width() * self.mainmenu_scale), int(self.mainmenu_d.get_height() * self.mainmenu_scale)))
            
            self.mainmenu_letter_blit[counter]

# class for pop-up whenever quitting or going back to main menu
class MainMenuQuit():
    def __init__(self, text:str, bg_img:tuple, surfacex:int, surfacey:int, scale:float):
        self.img = bg_img
        self.mainmenu_quit = pygame.transform.scale(self.img, (self.img.get_width() * scale, self.img.get_height() * scale))
        self.mainmenu_quit_rect = self.mainmenu_quit.get_rect()
        self.mainmenu_quit_rect.topleft = ((surfacex/2 - (self.mainmenu_quit.get_width()/2)), (surfacey/2 - (self.mainmenu_quit.get_height()/2)))
        self.mainmenu_quit_bg = pygame.Surface((surfacex, surfacey), pygame.SRCALPHA)
        self.mainmenu_quit_bg.fill((0,0,0,100))

        self.quit_line_font = pygame.font.FontType("assets/fonts/Sniglet-Regular.ttf", 30)
        self.quit_line_render = self.quit_line_font.render(text, False, (255, 255, 255))
        self.quit_line_shadow = self.quit_line_font.render(text, False, (0, 0, 72))

        self.line_scale_size = 1.2

        self.quit_line_render_resize = pygame.transform.scale(self.quit_line_render, (self.quit_line_render.get_width() * self.line_scale_size, self.quit_line_render.get_height() * self.line_scale_size))
        self.quit_line_shadow_resize = pygame.transform.scale(self.quit_line_shadow, (self.quit_line_shadow.get_width() * self.line_scale_size, self.quit_line_shadow.get_height() * self.line_scale_size))

        self.quit_linex = surfacex/2 - (self.quit_line_render_resize.get_width())/2
        self.quit_liney = surfacey/2 - (self.quit_line_render_resize.get_height())/2

        self.button_font = pygame.font.FontType("assets/fonts/Sniglet-ExtraBold.ttf", 40)
        self.quit_option1_render = self.button_font.render("YES", False, (255, 255, 255))
        self.quit_option2_render = self.button_font.render("NO", False, (255, 255, 255))

        self.quit_option1_shadow = self.button_font.render("YES", False, (0, 0, 72))
        self.quit_option2_shadow = self.button_font.render("NO", False, (0, 0, 72))

        self.scale_size = 1.3

        self.quit_option1_shadow_resize = pygame.transform.scale(self.quit_option1_shadow, (self.quit_option1_shadow.get_width() * self.scale_size, self.quit_option1_shadow.get_height() * self.scale_size))
        self.quit_option2_shadow_resize = pygame.transform.scale(self.quit_option2_shadow, (self.quit_option2_shadow.get_width() * self.scale_size, self.quit_option2_shadow.get_height() * self.scale_size))

        self.quit_option1x = surfacex/2 - (80 * self.scale_size)
        self.quit_option2x = surfacex/2 + (80 * self.scale_size)

        self.quit_optiony = surfacey/1.65
        self.quit_optiony_shadow = surfacey/1.65 + 5 * self.scale_size

        self.quit_option1_array = [self.quit_option1x, self.quit_optiony, [self.quit_option1_render, self.quit_option1_render], self.scale_size, 1, 1]
        self.quit_option2_array = [self.quit_option2x, self.quit_optiony, [self.quit_option2_render, self.quit_option2_render], self.scale_size, 1, 1]

        self.quit_option1 = button.ButtonController(self.quit_option1_array)
        self.quit_option2 = button.ButtonController(self.quit_option2_array)

        self.delay = False
        self.delay_return = dly.Delay()
        self.ctr = 0

        self.temp_value = None
        self.return_value = None

    def display(self, surface:tuple):
        # displays the window and the window bg
        surface.blit(self.mainmenu_quit_bg, (0, 0))
        surface.blit(self.mainmenu_quit, (self.mainmenu_quit_rect.x, self.mainmenu_quit_rect.y))
        surface.blit(self.quit_line_shadow_resize, (self.quit_linex, self.quit_liney))
        surface.blit(self.quit_line_render_resize, (self.quit_linex, self.quit_liney - (3 * self.line_scale_size)))
        surface.blit(self.quit_option1_shadow_resize, (self.quit_option1x - self.quit_option1_shadow_resize.get_width()/2, self.quit_optiony_shadow - self.quit_option1_shadow_resize.get_height()/2))
        surface.blit(self.quit_option2_shadow_resize, (self.quit_option2x - self.quit_option2_shadow_resize.get_width()/2, self.quit_optiony_shadow - self.quit_option2_shadow_resize.get_height()/2))
        
        # player choices buttons
        # if clicked, resume the game
        if self.quit_option2.button1(surface, True, True):
            self.quit_option2_array[1] = self.quit_optiony_shadow
            self.quit_option2 = button.ButtonController(self.quit_option2_array)
            self.temp_value = 'resume'
            self.delay = True
        else:
            self.quit_option2_array[1] = self.quit_optiony
            self.quit_option2 = button.ButtonController(self.quit_option2_array)

        # if clicked quit the game
        if self.quit_option1.button1(surface, True, True):
            self.quit_option1_array[1] = self.quit_optiony_shadow
            self.quit_option1 = button.ButtonController(self.quit_option1_array)
            self.temp_value = 'quit'
            self.delay = True
        else:
            self.quit_option1_array[1] = self.quit_optiony
            self.quit_option1 = button.ButtonController(self.quit_option1_array)
        
        if self.delay:
            if self.delay_return.delay(1, 10):
                self.return_value = self.temp_value
                self.delay_return.reset()
                self.delay = False
        else:
            self.return_value = 'stay'

        return self.return_value

class MainMenu():
    def __init__(self, surfacex:int, surfacey:int, surface:tuple):
        self.surfacex, self.surfacey = surfacex, surfacey
        self.surface = surface
        self.mainmenu = MainMenuTitle(surfacex/2, (surfacey/2)/2, 1.2, self.surface)
        self.mainmenu_bg = MainMenuBackground(surfacex, surfacey)

        music.Music.main_menu_music.play(-1)

        self.groupname_font = pygame.font.FontType("assets/fonts/balance_font.ttf", 20)
        self.groupname = self.groupname_font.render("Created by les problématiques", False, (255, 255, 255))
        self.version = self.groupname_font.render("Version 0.01", False, (255, 255, 255))

        self.button_font = pygame.font.FontType("assets/fonts/Karmatic.ttf", 40)
        self.play_render = self.button_font.render("PLAY", False, (255, 255, 255))
        self.quit_render = self.button_font.render("QUIT", False, (255, 255, 255))
        self.gm1_render = self.button_font.render("VS. BOT", False, (255, 255, 255))
        self.gm2_render = self.button_font.render("PVP", False, (255, 255, 255))
        self.back_render = self.button_font.render("BACK", False, (255, 255, 255))

        self.scale_size = 1.2
        self.default_butt_x1 = surfacex/2
        if self.surfacex == self.surfacey:
            self.offset = int(15 * self.scale_size)
        else:
            self.offset = int(9.5 * self.scale_size)
        self.default_butt_x2 = surfacex + (self.gm1_render.get_width() * self.scale_size) + self.offset
        self.bspace = (15 * self.scale_size)
        self.play_array = [self.default_butt_x1, (self.surfacey/2) + (self.surfacey/2)/4, [self.play_render, self.play_render], self.scale_size, 1.1, 2]
        self.quit_array = [self.default_butt_x1, self.play_array[1] + (self.surfacey/2)/4, [self.quit_render, self.quit_render], self.scale_size, 1.1, 2]
        self.gm1_array = [self.default_butt_x2, (self.surfacey/2) + (self.surfacey/2)/6, [self.gm1_render, self.gm1_render], self.scale_size, 1.1, 2]
        self.gm2_array = [self.default_butt_x2, self.gm1_array[1] + (self.surfacey/2)/6 + self.bspace, [self.gm2_render, self.gm2_render], self.scale_size, 1.1, 2]
        self.back_array = [self.default_butt_x2, self.gm2_array[1] + (self.surfacey/2)/6 + self.bspace, [self.back_render, self.back_render], self.scale_size, 1.1, 2]

        self.play = button.ButtonController(self.play_array)
        self.quit = button.ButtonController(self.quit_array)
        self.gm1 = button.ButtonController(self.gm1_array)
        self.gm2 = button.ButtonController(self.gm2_array)
        self.back = button.ButtonController(self.back_array)

        self.isActive = True
        self.isUpdate = True

        self.slideanim1 = animation.SlideAnimation(self.default_butt_x1)
        self.slideanim2 = animation.SlideAnimation(self.default_butt_x2)
        self.animate1 = False
        self.animate2 = False
        self.newxval1 = self.default_butt_x1
        self.newxval2 = self.default_butt_x2

        self.transition = False
        self.fadeto_anim = animation.FadeTo(self.surfacex, self.surfacey)

        self.mainmenu_quit = MainMenuQuit('Do you really wish to quit?', pygame.image.load("assets/imgs/mainmenu/mainmenu_quit1.png"),self.surfacex, self.surfacey, 1.7)
        self.mainmenu_quit_active = False

        self.delay_isActive = dly.Delay()

        self.return_value = 'main_menu'
        self.temp_value = None

        self.reset_delay = dly.Delay()

    def display(self):
        # mainmenu background
        self.mainmenu_bg.display(self.surface)
        # mainmenu title 
        self.mainmenu.displayMenu(self.surface)

        self.surface.blit(self.version, (self.surfacex - self.version.get_width(), self.surfacey - (self.version.get_height() + self.groupname.get_height())))
        self.surface.blit(self.groupname, (self.surfacex - self.groupname.get_width(), self.surfacey - self.groupname.get_height()))

        # play button in main menu
        # if clicked, go to gamemodes screen
        if self.play.button1(self.surface, self.isUpdate, self.isActive):
            self.animate1 = True
            self.isActive = False

        # quit button in main menu
        # if clicked, opens a window asking the player if he/she really wishes to quit
        if self.quit.button1(self.surface, self.isUpdate, self.isActive) == True:
            self.mainmenu_quit_active = True
        
        # game mode buttons in main menu
        # if clicked, proceed to VsBot gamemode
        if self.gm1.button1(self.surface, True, self.isActive):
            self.temp_value = 'gm1'
            self.transition = True

        # if clicked, proceed to PvP gamemode
        if self.gm2.button1(self.surface, True, self.isActive):
            self.temp_value = 'gm2'
            self.transition = True

        # if clicked, go back to play, quit screen
        if self.back.button1(self.surface, True, self.isActive):
            self.animate2 = True
            self.isActive = False

        # if true, display a window asking the player if he/she wants to quit
        if self.mainmenu_quit_active:
            if self.delay_isActive.delay(1, 5):
                self.isActive = False
                self.isUpdate = False
                self.delay_isActive.reset()
            quit_decision = self.mainmenu_quit.display(self.surface)
            if quit_decision == 'quit':
                self.return_value = 'quit'
            elif quit_decision == 'resume':
                self.mainmenu_quit_active = False
        else:
            self.isActive = True
            self.isUpdate = True

        # if true, animates the buttons
        if self.animate1:
            if self.newxval2 > self.surfacex/2:
                self.newxval1 = self.slideanim1.slide('left', 1)
                self.newxval2 = self.slideanim2.slide('left', 1)
                self.update()
            else:
                self.slideanim1.reset_param()
                self.slideanim2.reset_param()
                self.isActive = True
                self.animate1 = False
        
        # if true, animates the buttons
        if self.animate2:
            if self.newxval1 < self.surfacex/2:
                self.newxval1 = self.slideanim1.slide('right', 1)
                self.newxval2 = self.slideanim2.slide('right', 1)
                self.update()
            else:
                self.slideanim1.reset_param()
                self.slideanim2.reset_param()
                self.isActive = True
                self.animate2 = False
        
        # if true, fades the screen to black
        if self.transition:
            self.isActive = False
            if self.fadeto_anim.fade(3, self.surface) >= 255:
                self.return_value = self.temp_value
                self.fadeto_anim.reset()
                music.Music.main_menu_music.fadeout(10)
                self.transition = False

        return self.return_value
    
    # updates x values of buttons
    def update(self):
        self.play_array[0] = self.newxval1
        self.quit_array[0] = self.newxval1
        self.gm1_array[0] = self.newxval2
        self.gm2_array[0] = self.newxval2
        self.back_array[0] = self.newxval2
        self.play = button.ButtonController(self.play_array)
        self.quit = button.ButtonController(self.quit_array)
        self.gm1 = button.ButtonController(self.gm1_array)
        self.gm2 = button.ButtonController(self.gm2_array)
        self.back = button.ButtonController(self.back_array)

    # resets the variables self.return_value and self.reset_delay
    def reset(self):
        music.Music.main_menu_music.play(-1)
        self.return_value = 'main_menu'
        if self.reset_delay.delay(1, 100):
            self.reset_delay.reset()