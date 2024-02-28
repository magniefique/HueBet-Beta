import pygame
import classes.button as btn
import classes.delay as dly
import classes.loading as load
import classes.animation as anim
import classes.main_menu as mm
import classes.music as music
import random

class VsBot():
    def __init__(self, surfacex:int, surfacey:int, surface:tuple):
        # window variables 
        self.surface = surface
        self.surfacex, self.surfacey = surfacex, surfacey

        # load the img assets
        self.bg_img = pygame.image.load("assets/imgs/maingame/game_bg.png").convert_alpha()
        self.bal_ui_img1 = pygame.image.load("assets/imgs/maingame/balance/game_playerbalance.png").convert_alpha()
        self.bal_ui_img2 = pygame.image.load("assets/imgs/maingame/balance/game_botbalance.png").convert_alpha()
        self.enemybot_neutral_img = pygame.image.load("assets/imgs/maingame/enemy_bot/robot_neutral.png").convert_alpha()
        self.enemybot_happy_img = pygame.image.load("assets/imgs/maingame/enemy_bot/robot_happy.png").convert_alpha()
        self.enemybot_sad_img = pygame.image.load("assets/imgs/maingame/enemy_bot/robot_sad.png").convert_alpha()
        self.table_img = pygame.image.load("assets/imgs/maingame/game_table.png").convert_alpha()
        self.rndmizer_img = pygame.image.load("assets/imgs/maingame/game_randomizer.png").convert_alpha()
        self.ui_img = pygame.image.load("assets/imgs/maingame/game_ui1.png").convert_alpha()
        self.enemybot_betcontainer_img = pygame.image.load("assets/imgs/maingame/bet_container/game_botbetcontainer.png")

        # resize the assets
        self.scale = surfacex/self.bg_img.get_width(), surfacey/self.bg_img.get_height()
        self.bg = pygame.transform.scale(self.bg_img, (self.bg_img.get_width() * self.scale[0], self.bg_img.get_height() * self.scale[1]))
        self.bal_ui1 = pygame.transform.scale(self.bal_ui_img1, (self.bal_ui_img1.get_width() * self.scale[0], self.bal_ui_img1.get_height() * self.scale[1]))
        self.bal_ui2 = pygame.transform.scale(self.bal_ui_img2, (self.bal_ui_img2.get_width() * self.scale[0], self.bal_ui_img2.get_height() * self.scale[1]))
        self.enemybot_neutral = pygame.transform.scale(self.enemybot_neutral_img, (self.enemybot_neutral_img.get_width() * self.scale[1]/1.6, self.enemybot_neutral_img.get_height() * self.scale[1]/1.6))
        self.enemybot_happy = pygame.transform.scale(self.enemybot_happy_img, (self.enemybot_happy_img.get_width() * self.scale[1]/1.6, self.enemybot_happy_img.get_height() * self.scale[1]/1.6))
        self.enemybot_sad = pygame.transform.scale(self.enemybot_sad_img, (self.enemybot_sad_img.get_width() * self.scale[1]/1.6, self.enemybot_sad_img.get_height() * self.scale[1]/1.6))
        self.table = pygame.transform.scale(self.table_img, (self.table_img.get_width() * self.scale[0], self.table_img.get_height() * self.scale[1]))
        self.rndmizer = pygame.transform.scale(self.rndmizer_img, (self.rndmizer_img.get_width() * self.scale[1], self.rndmizer_img.get_height() * self.scale[1]))
        self.ui = pygame.transform.scale(self.ui_img, (self.ui_img.get_width() * self.scale[1], self.ui_img.get_height() * self.scale[1]))
        self.enemybot_betcontainer = pygame.transform.scale(self.enemybot_betcontainer_img, (self.enemybot_betcontainer_img.get_width() * self.scale[1], self.enemybot_betcontainer_img.get_height() * self.scale[1]))

        # enemybot img array
        self.enemybot = [self.enemybot_neutral, self.enemybot_happy, self.enemybot_sad]
        self.enemybot_ctr = 0

        # load enemybot color choices
        self.enemybot_red_img = pygame.image.load("assets/imgs/maingame/enemy_choice/red.png").convert_alpha()
        self.enemybot_green_img = pygame.image.load("assets/imgs/maingame/enemy_choice/green.png").convert_alpha()
        self.enemybot_blue_img = pygame.image.load("assets/imgs/maingame/enemy_choice/blue.png").convert_alpha()
        self.enemybot_pink_img = pygame.image.load("assets/imgs/maingame/enemy_choice/pink.png").convert_alpha()
        self.enemybot_yellow_img = pygame.image.load("assets/imgs/maingame/enemy_choice/yellow.png").convert_alpha()
        self.enemybot_violet_img = pygame.image.load("assets/imgs/maingame/enemy_choice/violet.png").convert_alpha()

        # resize enemybot color choices
        self.enemybot_red = pygame.transform.scale(self.enemybot_red_img, (self.enemybot_red_img.get_width() * self.scale[1], self.enemybot_red_img.get_height() * self.scale[1]))
        self.enemybot_green = pygame.transform.scale(self.enemybot_green_img, (self.enemybot_green_img.get_width() * self.scale[1], self.enemybot_green_img.get_height() * self.scale[1]))
        self.enemybot_blue = pygame.transform.scale(self.enemybot_blue_img, (self.enemybot_blue_img.get_width() * self.scale[1], self.enemybot_blue_img.get_height() * self.scale[1]))
        self.enemybot_pink = pygame.transform.scale(self.enemybot_pink_img, (self.enemybot_pink_img.get_width() * self.scale[1], self.enemybot_pink_img.get_height() * self.scale[1]))
        self.enemybot_yellow = pygame.transform.scale(self.enemybot_yellow_img, (self.enemybot_yellow_img.get_width() * self.scale[1], self.enemybot_yellow_img.get_height() * self.scale[1]))
        self.enemybot_violet = pygame.transform.scale(self.enemybot_violet_img, (self.enemybot_violet_img.get_width() * self.scale[1], self.enemybot_violet_img.get_height() * self.scale[1]))

        # load lightbulb colors
        self.clr_default_img = pygame.image.load("assets/imgs/maingame/color_result/default.png").convert_alpha()
        self.clr_red_img = pygame.image.load("assets/imgs/maingame/color_result/red.png").convert_alpha()
        self.clr_green_img = pygame.image.load("assets/imgs/maingame/color_result/green.png").convert_alpha()
        self.clr_blue_img = pygame.image.load("assets/imgs/maingame/color_result/blue.png").convert_alpha()
        self.clr_pink_img = pygame.image.load("assets/imgs/maingame/color_result/pink.png").convert_alpha()
        self.clr_yellow_img = pygame.image.load("assets/imgs/maingame/color_result/yellow.png").convert_alpha()
        self.clr_violet_img = pygame.image.load("assets/imgs/maingame/color_result/violet.png").convert_alpha()

        # resize lightbulbs
        self.clr_default = pygame.transform.scale(self.clr_default_img, (self.clr_default_img.get_width() * self.scale[1], self.clr_default_img.get_height() * self.scale[1]))
        self.clr_red = pygame.transform.scale(self.clr_red_img, (self.clr_red_img.get_width() * self.scale[1], self.clr_red_img.get_height() * self.scale[1]))
        self.clr_green = pygame.transform.scale(self.clr_green_img, (self.clr_green_img.get_width() * self.scale[1], self.clr_green_img.get_height() * self.scale[1]))
        self.clr_blue = pygame.transform.scale(self.clr_blue_img, (self.clr_blue_img.get_width() * self.scale[1], self.clr_blue_img.get_height() * self.scale[1]))
        self.clr_pink = pygame.transform.scale(self.clr_pink_img, (self.clr_pink_img.get_width() * self.scale[1], self.clr_pink_img.get_height() * self.scale[1]))
        self.clr_yellow = pygame.transform.scale(self.clr_yellow_img, (self.clr_yellow_img.get_width() * self.scale[1], self.clr_yellow_img.get_height() * self.scale[1]))
        self.clr_violet = pygame.transform.scale(self.clr_violet_img, (self.clr_violet_img.get_width() * self.scale[1], self.clr_violet_img.get_height() * self.scale[1]))

        # array for all lightbulb colors
        self.clr_result = [self.clr_default, self.clr_red, self.clr_green, self.clr_blue, self.clr_pink, self.clr_yellow, self.clr_violet]
        
        # array for all colors
        self.colors = ['default', 'red', 'green', 'blue', 'pink', 'yellow', 'violet']

        # asset rect x and y position
        # enemybot rect values
        self.enemybot_rect = self.enemybot[0].get_rect()
        self.enemybot_rect.topleft = (self.surfacex/2 - self.enemybot[0].get_width()/2, self.surfacey/2 - (self.enemybot[0].get_height()/2))
        
        # randomizer rect values
        self.rndmizer_rect = self.rndmizer.get_rect()
        self.rndmizer_rect.topleft = (self.surfacex/2 - self.rndmizer.get_width()/2, (self.surfacey/2) + (50 * self.scale[1]))
        
        # balance ui rect values
        self.bal_ui1_rect = self.bal_ui1.get_rect()
        self.bal_ui1_rect.topleft = (0 - self.bal_ui1.get_width(), 0)
        self.bal_ui1_finalleft = 0
        self.bal_ui2_rect = self.bal_ui2.get_rect()
        self.bal_ui2_rect.topright = (self.surfacex + self.bal_ui2.get_width(), 0)
        self.bal_ui2_finalright = self.surfacex
        
        # player ui rect values
        self.ui_rect = self.ui.get_rect()
        self.ui_rect.topleft = (self.surfacex/2 - self.ui.get_width()/2, self.surfacey + (120 * self.scale[1]))
        
        # enemybot bet container rect values
        self.enemybot_betcontainer_rect = self.enemybot_betcontainer.get_rect()
        self.enemybot_betcontainer_y = self.enemybot_rect.top - (self.enemybot_betcontainer.get_height() + (16 * self.scale[1]))
        self.enemybot_betcontainer_rect.topleft = self.surfacex/2 - self.enemybot_betcontainer.get_width()/2, self.enemybot_betcontainer_y

        # amount of space between enemybot choices
        self.enemybot_space = (4 * self.scale[1])

        # enemybot choice x and y
        self.enemybot_blue_x = (self.surfacex/2 - self.enemybot_blue.get_width()/2) - ((self.enemybot_blue.get_width()/2) + self.enemybot_space)
        self.enemybot_green_x = self.enemybot_blue_x - (self.enemybot_green.get_width() + self.enemybot_space * 2)
        self.enemybot_red_x = self.enemybot_green_x - (self.enemybot_red.get_width() + self.enemybot_space * 2)
        self.enemybot_pink_x = (self.surfacex/2 - self.enemybot_pink.get_width()/2) + ((self.enemybot_pink.get_width()/2) + self.enemybot_space)
        self.enemybot_yellow_x = self.enemybot_pink_x + (self.enemybot_yellow.get_width() + self.enemybot_space * 2)
        self.enemybot_violet_x = self.enemybot_yellow_x + (self.enemybot_violet.get_width() + self.enemybot_space * 2)

        # load all button assets
        self.btn_red_img = pygame.image.load("assets/imgs/maingame/button/red.png").convert_alpha()
        self.btn_red_active_img = pygame.image.load("assets/imgs/maingame/button_active/red.png").convert_alpha()

        self.btn_green_img = pygame.image.load("assets/imgs/maingame/button/green.png").convert_alpha()
        self.btn_green_active_img = pygame.image.load("assets/imgs/maingame/button_active/green.png").convert_alpha()

        self.btn_blue_img = pygame.image.load("assets/imgs/maingame/button/blue.png").convert_alpha()
        self.btn_blue_active_img = pygame.image.load("assets/imgs/maingame/button_active/blue.png").convert_alpha()

        self.btn_pink_img = pygame.image.load("assets/imgs/maingame/button/pink.png").convert_alpha()
        self.btn_pink_active_img = pygame.image.load("assets/imgs/maingame/button_active/pink.png").convert_alpha()

        self.btn_yellow_img = pygame.image.load("assets/imgs/maingame/button/yellow.png").convert_alpha()
        self.btn_yellow_active_img = pygame.image.load("assets/imgs/maingame/button_active/yellow.png").convert_alpha()

        self.btn_violet_img = pygame.image.load("assets/imgs/maingame/button/violet.png").convert_alpha()
        self.btn_violet_active_img = pygame.image.load("assets/imgs/maingame/button_active/violet.png").convert_alpha()

        self.btn_bet_img = pygame.image.load("assets/imgs/maingame/button/bet.png").convert_alpha()
        self.btn_bet_active_img = pygame.image.load("assets/imgs/maingame/button_active/bet.png").convert_alpha()

        self.btn_menu_img = pygame.image.load("assets/imgs/maingame/menu_button/menu1.png").convert_alpha()
        self.btn_menu_active_img = pygame.image.load("assets/imgs/maingame/menu_button/menu2.png").convert_alpha()

        # button additional position values
        self.ui_margin = (48 * self.scale[1])
        self.btn_dimen = (48 * self.scale[1], 48 * self.scale[1])
        self.btn_space = 25 * self.scale[1]

        # button arrays
        # button array for color choices
        self.btn_red_array = [self.ui_rect.left + (self.btn_dimen[1]/2) + self.ui_margin, self.ui_rect.centery - (12 * self.scale[1]), [self.btn_red_img, self.btn_red_active_img], self.scale[1], 1, 1]
        self.btn_green_array = [self.btn_red_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_green_img, self.btn_green_active_img], self.scale[1], 1, 1]
        self.btn_blue_array = [self.btn_green_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_blue_img, self.btn_blue_active_img], self.scale[1], 1, 1]
        self.btn_pink_array = [self.btn_blue_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_pink_img, self.btn_pink_active_img], self.scale[1], 1, 1]
        self.btn_yellow_array = [self.btn_pink_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_yellow_img, self.btn_yellow_active_img], self.scale[1], 1, 1]
        self.btn_violet_array = [self.btn_yellow_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_violet_img, self.btn_violet_active_img], self.scale[1], 1, 1]

        # button array for bet button
        self.btn_bet_array = [self.ui_rect.right - ((96 * self.scale[1]/2) + self.ui_margin), self.ui_rect.centery - (16 * self.scale[1]), [self.btn_bet_img, self.btn_bet_active_img], self.scale[1], 1.05, 1]
        
        # button array for main menu button
        self.btn_menu_array = [self.ui_rect.left + ((self.btn_menu_img.get_width()/2 * self.scale[1]) + (8 * self.scale[1])), self.ui_rect.top - ((self.btn_menu_img.get_height()/2 * self.scale[1]) + (2 * self.scale[1])), [self.btn_menu_img, self.btn_menu_active_img], self.scale[1], 1, 1]

        # button initializtation
        self.btn_state = False
        self.btn_state_menu = False
        self.btn_update = True
        self.btn_red = btn.ButtonController(self.btn_red_array)
        self.btn_green = btn.ButtonController(self.btn_green_array)
        self.btn_blue = btn.ButtonController(self.btn_blue_array)
        self.btn_pink = btn.ButtonController(self.btn_pink_array)
        self.btn_yellow = btn.ButtonController(self.btn_yellow_array)
        self.btn_violet = btn.ButtonController(self.btn_violet_array)
        
        # bet button
        self.btn_bet = btn.ButtonController(self.btn_bet_array)

        # menu button
        self.btn_menu = btn.ButtonController(self.btn_menu_array)

        # font initialization
        self.font_round = pygame.font.FontType("assets/fonts/upheavtt.ttf", 64)
        self.font_round_small = pygame.font.FontType("assets/fonts/upheavtt.ttf", 32)
        self.font_timer = pygame.font.FontType("assets/fonts/upheavtt.ttf", 64)
        self.font_num = pygame.font.FontType("assets/fonts/balance_font.ttf", 32)
        
        # text balance colors
        self.clr_balance_green = (57, 255, 20)
        self.clr_balance_red = (255, 49, 49)

        # initial colors for balances
        self.clr_balance1 = self.clr_balance_green
        self.clr_balance2 = self.clr_balance_green

        # loading screen
        self.loading = load.Loading(self.surfacex, self.surfacey)
        self.loading_quit = load.Loading(self.surfacex, self.surfacey)
        
        # bool var responsible for activating loadscreen before going back to main menu
        self.loadscreen_quit = False

        # fade in animation at start
        self.fadefrom_active = True
        self.fadefrom = anim.FadeFrom(self.surfacex, self.surfacey)

        # initial animation
        self.initial_anim = True

        # bet container animation
        self.enemybot_betcontainer_anim = anim.HoverAnimation()

        # text color values
        self.maintxt_clr = (255, 255, 255)
        self.shadow_clr = (1, 59, 96)

        # variables for displaying the round count each round
        # initialization of delay before round start
        self.round_delay = dly.Delay()

        # bool var responsible of animating the round count
        self.round_start = False

        # initial state of the animation
        self.round_state = 'fadebg'

        # bg of the animation
        self.round_surface = pygame.Surface((self.surfacex, self.surfacey))
        self.round_surface.fill((0, 0, 0))

        # initial alpha value of the bg
        self.round_surface_alpha = 0

        # variable that holds the round count
        self.round_count = 1

        # renders the necessary round text to be displayed on the screen
        self.round_count_render = self.font_round.render("ROUND " + (str(self.round_count)), False, self.maintxt_clr)
        self.round_shadow_render = self.font_round.render("ROUND " + (str(self.round_count)), False, self.shadow_clr)
        
        # resizes the round text 
        self.round_count_display = pygame.transform.scale(self.round_count_render, (self.round_count_render.get_width() * (self.scale[1] * 2), self.round_count_render.get_height() * (self.scale[1] * 2)))
        self.round_shadow_display = pygame.transform.scale(self.round_shadow_render, (self.round_shadow_render.get_width() * (self.scale[1] * 2), self.round_shadow_render.get_height() * (self.scale[1] * 2)))
        
        # x and y values of the round count
        self.round_x = 0 - (self.round_count_display.get_width() + (40 * self.scale[1]))
        self.round_y = self.surfacey/2 - self.round_count_display.get_height()/2

        # timer variables
        # initializes delay before timer becomes active
        self.timer_active_delay = dly.Delay()

        # bool var responsible of activating timer
        self.timer_active = False
        
        # timer values
        self.timer_default_value = 30
        self.timer_value = self.timer_default_value
        
        # initializes delay for each decrease of timer value
        self.timer_delay = dly.Delay()

        # initial bet value
        self.bet_val = 10

        # player balance variable
        self.plyr_bal = 1000

        # array that keeps player choice
        self.plyr_choice = []

        # if true, refunds the player's balance if unclicking a button
        self.plyr_refund = True
        
        # enemybot balance variable
        self.enemybot_bal = 1000

        # maximum count of color that enemybot can bet
        self.enemybot_max_bet = None

        # number of bet the bot chooses
        self.enemybot_betcount = None
        
        # the color the bot chooses
        self.enemybot_bet_clr = None

        # array that stores all the color the bot chooses
        self.enemybot_choice = []

        # colorgame variables
        # bool var responsible for starting the randomization of colors
        self.colorgame = False

        # bool var responsible for animating assets for randomization of colors
        self.colorgame_anim = False

        # counters used for the animations 
        self.colorgame_anim_ctr1 = 0
        self.colorgame_anim_ctr2 = 0

        # initial state of the colorgame animation
        self.colorgame_anim_state = 'update'

        # delays each color appearance in the animation
        self.colorgame_delay = dly.Delay()

        # win amount display
        # bool var responsible for displaying add in the balance
        self.displayadd = False

        # display add values
        self.plyr_displayadd = 0
        self.enemybot_displayadd = 0

        # result variables
        self.result_randomize = None
        self.result_str = []
        self.temp_result = []

        # initial values for final result
        self.final_result = [0, 0, 0]

        # partial reset variables
        self.reset = False
        self.reset_delay = dly.Delay()

        # variables for displaying winner
        # variable of winner
        self.winner = None

        # bool var resposible of displaying winner 
        self.winner_isActive = False

        # initial state of display animation of winner
        self.winner_state = 'fadefrom'

        # bg of winner display
        self.winner_bg = pygame.Surface((self.surfacex, self.surfacey))
        
        # initial alpha value of bg of winner display
        self.winner_bg_alpha = 0

        # initialization of delay for displaying message after displaying winner
        self.winner_displaymes_delay = dly.Delay()

        # text render for the message after displaying winner
        self.winner_displaymes_render = self.font_round_small.render('CLICK ANYWHERE TO CONTINUE', False, self.maintxt_clr)
        self.winner_displaymes_shadow_render = self.font_round_small.render('CLICK ANYWHERE TO CONTINUE', False, self.shadow_clr)

        # resize text render for the message
        self.winner_displaymes = pygame.transform.scale(self.winner_displaymes_render, (self.winner_displaymes_render.get_width() * self.scale[1], self.winner_displaymes_render.get_height() * self.scale[1]))
        self.winner_displaymes_shadow = pygame.transform.scale(self.winner_displaymes_shadow_render, (self.winner_displaymes_shadow_render.get_width() * self.scale[1], self.winner_displaymes_shadow_render.get_height() * self.scale[1]))
        self.winner_displaymes_anim = anim.FadeInOut()

        # main menu variables
        # bool var responsible for displaying menu
        self.menu_isActive = False
        self.menu_display = mm.MainMenuQuit('Your progress won\'t be saved.', pygame.image.load("assets/imgs/mainmenu/mainmenu_quit2.png"), self.surfacex, self.surfacey, 1.7)

        # state variable of the game
        self.return_value = 'gm1'

    def display(self):
        # loadscreen before game start
        if self.loading.load(150, self.surface):
            # display the background assets
            self.surface.blit(self.bg, (0, 0))
            self.surface.blit(self.bal_ui1, (self.bal_ui1_rect.x, self.bal_ui1_rect.y))
            self.surface.blit(self.bal_ui2, (self.bal_ui2_rect.x, self.bal_ui2_rect.y))
            
            # display enemybot
            # if displaying additional value in balance,
            # if self.enemybot_displayadd is not 0, display happy emotion
            # if self.enemybot_displayadd is 0, display sad emotion
            # if not displaying additional value in balance, display neutral emotion
            if self.displayadd:
                if self.enemybot_displayadd != 0:
                    self.enemybot_ctr = 1
                else:
                    self.enemybot_ctr = 2
            else:
                self.enemybot_ctr = 0
            self.surface.blit(self.enemybot[self.enemybot_ctr], (self.enemybot_rect.x, self.enemybot_rect.y))
            
            # display table
            self.surface.blit(self.table, (0, self.surfacey - (self.table.get_height() - (20 * self.scale[1]))))
            
            # display color randomizer
            self.surface.blit(self.rndmizer, (self.rndmizer_rect.x, self.rndmizer_rect.y))
        
            # display result colors
            self.surface.blit(self.clr_result[self.final_result[0]], ((self.surfacex/2 - self.clr_result[0].get_width()/2) - ((20 * self.scale[1]) + (self.clr_result[0].get_width())), (self.rndmizer_rect.top + (7.5 * self.scale[1])) - self.clr_result[0].get_height()))
            self.surface.blit(self.clr_result[self.final_result[1]], (self.surfacex/2 - self.clr_result[0].get_width()/2, (self.rndmizer_rect.top + (7.5 * self.scale[1])) - self.clr_result[0].get_height()))
            self.surface.blit(self.clr_result[self.final_result[2]], ((self.surfacex/2 - self.clr_result[0].get_width()/2) + ((20 * self.scale[1]) + (self.clr_result[0].get_width())), (self.rndmizer_rect.top + (7.5 * self.scale[1])) - self.clr_result[0].get_height()))

            # display player ui (button container)
            self.surface.blit(self.ui, (self.ui_rect.x, self.ui_rect.y))
            
            # display buttons
            red_bet = self.btn_red.button2(self.surface, self.btn_update, self.btn_state)
            green_bet = self.btn_green.button2(self.surface, self.btn_update, self.btn_state)
            blue_bet = self.btn_blue.button2(self.surface, self.btn_update, self.btn_state)
            pink_bet = self.btn_pink.button2(self.surface, self.btn_update, self.btn_state)
            yellow_bet = self.btn_yellow.button2(self.surface, self.btn_update, self.btn_state)
            violet_bet = self.btn_violet.button2(self.surface, self.btn_update, self.btn_state)

            # displays enemybbt bet
            # enemybot betcontainer animation
            self.enemybot_betcontainer_rect.y = self.enemybot_betcontainer_anim.hover(self.enemybot_betcontainer_y, 4, 0.06)

            # displays the bet container 
            self.surface.blit(self.enemybot_betcontainer, (self.enemybot_betcontainer_rect.x, self.enemybot_betcontainer_rect.y))
            
            # check if self.enemybot_choice is not empty and if true, display colors in self.enemybot_choice
            if self.enemybot_choice != []:
                if 'red' in self.enemybot_choice:
                    self.surface.blit(self.enemybot_red, (self.enemybot_red_x, self.enemybot_betcontainer_rect.y + (8 * self.scale[1])))
                if 'green' in self.enemybot_choice:
                    self.surface.blit(self.enemybot_green, (self.enemybot_green_x, self.enemybot_betcontainer_rect.y + (8 * self.scale[1])))
                if 'blue' in self.enemybot_choice:
                    self.surface.blit(self.enemybot_blue, (self.enemybot_blue_x, self.enemybot_betcontainer_rect.y + (8 * self.scale[1])))
                if 'pink' in self.enemybot_choice:
                    self.surface.blit(self.enemybot_pink, (self.enemybot_pink_x, self.enemybot_betcontainer_rect.y + (8 * self.scale[1])))
                if 'yellow' in self.enemybot_choice:        
                    self.surface.blit(self.enemybot_yellow, (self.enemybot_yellow_x, self.enemybot_betcontainer_rect.y + (8 * self.scale[1])))
                if 'violet' in self.enemybot_choice:
                    self.surface.blit(self.enemybot_violet, (self.enemybot_violet_x, self.enemybot_betcontainer_rect.y + (8 * self.scale[1])))

            # display timer
            self.timer_render = self.font_timer.render(str(self.timer_value), False, self.maintxt_clr)
            self.timer_shadow_render = self.font_timer.render(str(self.timer_value), False, self.shadow_clr)
            self.timer = pygame.transform.scale(self.timer_render, (self.timer_render.get_width() * self.scale[1], self.timer_render.get_height() * self.scale[1]))
            self.timer_shadow = pygame.transform.scale(self.timer_shadow_render, (self.timer_shadow_render.get_width() * self.scale[1], self.timer_shadow_render.get_height() * self.scale[1]))
            self.surface.blit(self.timer_shadow, (self.surfacex/2 - self.timer.get_width()/2, 17 * self.scale[1]))
            self.surface.blit(self.timer, (self.surfacex/2 - self.timer.get_width()/2, 12 * self.scale[1]))

            # display round count under timer
            self.round_small_render = self.font_round_small.render('ROUND ' + str(self.round_count), False, self.maintxt_clr)
            self.round_small_shadow = self.font_round_small.render('ROUND ' + str(self.round_count), False, self.shadow_clr)
            self.round_small_display = pygame.transform.scale(self.round_small_render, (self.round_small_render.get_width() * self.scale[1]/1.5, self.round_small_render.get_height() * self.scale[1]/1.5))
            self.round_small_shadow_display =  pygame.transform.scale(self.round_small_shadow, (self.round_small_shadow.get_width() * self.scale[1]/1.5, self.round_small_shadow.get_height() * self.scale[1]/1.5))
            self.surface.blit(self.round_small_shadow_display, (self.surfacex/2 - self.round_small_display.get_width()/2, 75 * self.scale[1] + (3 * self.scale[1]/1.5)))
            self.surface.blit(self.round_small_display, (self.surfacex/2 - self.round_small_display.get_width()/2, 75 * self.scale[1]))

            # display bet value
            self.bet_display_render = self.font_num.render(str(self.bet_val), False, self.clr_balance_green)
            self.bet_display = pygame.transform.scale(self.bet_display_render, (self.bet_display_render.get_width() * self.scale[1], self.bet_display_render.get_height() * self.scale[1]))
            self.surface.blit(self.bet_display, (self.rndmizer_rect.centerx - self.bet_display.get_width()/2, (self.rndmizer_rect.centery - self.bet_display.get_height()/2) - (20 * self.scale[1])))

            # display balance of player and enemybot
            if self.plyr_bal >= self.bet_val:
                self.clr_balance1 = self.clr_balance_green
            else:
                self.clr_balance1 = self.clr_balance_red

            self.plyr_bal_render = self.font_num.render(str(self.plyr_bal), False, self.clr_balance1)
            self.plyr_bal_display = pygame.transform.scale(self.plyr_bal_render, (self.plyr_bal_render.get_width() * self.scale[1], self.plyr_bal_render.get_height() * self.scale[1]))
            self.plyr_bal_uiy = self.bal_ui1_rect.bottom - (self.plyr_bal_display.get_height() + self.ui_margin/3)
            self.surface.blit(self.plyr_bal_display, (self.bal_ui1_rect.right - (self.plyr_bal_display.get_width() + self.ui_margin/2), self.plyr_bal_uiy))

            if self.enemybot_bal >= self.bet_val:
                self.clr_balance2 = self.clr_balance_green
            else:
                self.clr_balance2 = self.clr_balance_red

            self.enemybot_bal_render = self.font_num.render(str(self.enemybot_bal), False, self.clr_balance2)
            self.enemybot_bal_display = pygame.transform.scale(self.enemybot_bal_render, (self.enemybot_bal_render.get_width() * self.scale[1], self.enemybot_bal_render.get_height() * self.scale[1]))
            self.surface.blit(self.enemybot_bal_display, (self.bal_ui2_rect.right - (self.enemybot_bal_display.get_width() + self.ui_margin/2), self.plyr_bal_uiy))

            # display balance add of both player and enemybot after each round
            if self.displayadd:
                if self.plyr_displayadd != 0:
                    self.plyr_displayadd_render = self.font_num.render('+' + str(self.plyr_displayadd), False, self.clr_balance_green)
                    self.plyr_displayadd_display = pygame.transform.scale(self.plyr_displayadd_render, (self.plyr_displayadd_render.get_width() * self.scale[1], self.plyr_displayadd_render.get_height() * self.scale[1]))
                    self.surface.blit(self.plyr_displayadd_display, (self.bal_ui1_rect.left + self.ui_margin/2, self.plyr_bal_uiy))
                if self.enemybot_displayadd != 0:
                    self.enemybot_displayadd_render = self.font_num.render('+' + str(self.enemybot_displayadd), False, self.clr_balance_green)
                    self.enemybot_displayadd_display = pygame.transform.scale(self.enemybot_displayadd_render, (self.enemybot_displayadd_render.get_width() * self.scale[1], self.enemybot_displayadd_render.get_height() * self.scale[1]))
                    self.surface.blit(self.enemybot_displayadd_display, (self.bal_ui2_rect.left + self.ui_margin/2, self.plyr_bal_uiy))

            
            # Checks the color buttons pressed, if clicked while not activated, add color to array self.plyr_choice and
            # decrease self.plyr_bal depending on value of self.bet_val. If button is already activated and player decides
            # to click it, the certain color will be removed from self.plyr_choice and players balance will add depending on
            # value of self.bet_val
            
            # for red button
            if red_bet:
                if self.plyr_bal >= self.bet_val:
                    if 'red' not in self.plyr_choice:
                        self.plyr_choice.append('red')
                        self.plyr_bal -= self.bet_val
                elif 'red' not in self.plyr_choice:
                    self.btn_red.button2reset(self.surface)
            elif not red_bet and 'red' in self.plyr_choice:
                self.plyr_choice.remove('red')
                if self.plyr_refund:
                    self.plyr_bal += self.bet_val
            
            # for green button
            if green_bet:
                if self.plyr_bal >= self.bet_val:
                    if 'green' not in self.plyr_choice:
                        self.plyr_choice.append('green')
                        self.plyr_bal -= self.bet_val
                elif 'green' not in self.plyr_choice:
                    self.btn_green.button2reset(self.surface)
            elif not green_bet and 'green' in self.plyr_choice:
                self.plyr_choice.remove('green')
                if self.plyr_refund:
                    self.plyr_bal += self.bet_val
            
            # for blue button
            if blue_bet:
                if self.plyr_bal >= self.bet_val:
                    if 'blue' not in self.plyr_choice:
                        self.plyr_choice.append('blue')
                        self.plyr_bal -= self.bet_val
                elif 'blue' not in self.plyr_choice:
                    self.btn_blue.button2reset(self.surface)
            elif not blue_bet and 'blue' in self.plyr_choice:
                self.plyr_choice.remove('blue')
                if self.plyr_refund:
                    self.plyr_bal += self.bet_val
            
            # for pink button
            if pink_bet:
                if self.plyr_bal >= self.bet_val:
                    if 'pink' not in self.plyr_choice:
                        self.plyr_choice.append('pink')
                        self.plyr_bal -= self.bet_val
                elif 'pink' not in self.plyr_choice:
                    self.btn_pink.button2reset(self.surface)
            elif not pink_bet and 'pink' in self.plyr_choice:
                self.plyr_choice.remove('pink')
                if self.plyr_refund:
                    self.plyr_bal += self.bet_val
            
            # for yellow button
            if yellow_bet:
                if self.plyr_bal >= self.bet_val:
                    if 'yellow' not in self.plyr_choice:
                        self.plyr_choice.append('yellow')
                        self.plyr_bal -= self.bet_val
                elif 'yellow' not in self.plyr_choice:
                    self.btn_yellow.button2reset(self.surface)
            elif not yellow_bet and 'yellow' in self.plyr_choice:
                self.plyr_choice.remove('yellow')
                if self.plyr_refund:
                    self.plyr_bal += self.bet_val
            
            # for violet button
            if violet_bet:
                if self.plyr_bal >= self.bet_val:
                    if 'violet' not in self.plyr_choice:
                        self.plyr_choice.append('violet')
                        self.plyr_bal -= self.bet_val
                elif 'violet' not in self.plyr_choice:
                    self.btn_violet.button2reset(self.surface)
            elif not violet_bet and 'violet' in self.plyr_choice:
                self.plyr_choice.remove('violet')
                if self.plyr_refund:
                    self.plyr_bal += self.bet_val

            # bet button
            # if clicked, check if player has no bet, if true, decrease player
            # balance value by half of the value of self.bet_val variable then 
            # proceed on animating the lightbulbs 
            if self.btn_bet.button1(self.surface, self.btn_update, self.btn_state):
                if self.plyr_choice == []:
                    self.plyr_bal -= int(self.bet_val/2)
                self.enemybot_bet()
                self.timer_active = False
                self.timer_value = self.timer_default_value
                self.colorgame_anim = True
                self.btn_state = False

            # menu button
            # if clicked, display a window asking if the player really wishes to quit or not
            if self.btn_menu.button1(self.surface, True, self.btn_state_menu):
                self.btn_state = False
                self.btn_state_menu = False
                self.btn_update = False
                self.menu_isActive = True
                
            # fade animation at start
            if self.fadefrom_active:
                if self.fadefrom.fade(5, self.surface) <= 0:
                    if self.round_delay.delay(1, 10):
                        music.Music.ingame_music1.play(-1)
                        self.fadefrom_active = False
                        self.btn_state_menu = True

            # initial animation
            if self.initial_anim:
                if self.bal_ui1_rect.left < self.bal_ui1_finalleft and self.bal_ui2_rect.right > self.bal_ui2_finalright:
                    self.bal_ui1_rect.left += 3
                    self.bal_ui2_rect.right -= 3
                else:
                    if self.ui_rect.bottom > self.surfacey:
                        self.updatebuttons()
                        self.ui_rect.top -= 4
                    else:
                        self.initial_anim = False
                        self.round_start = True

            # round indicator animation 
            if self.round_start:
                self.round_display()

            # activates timer 
            if self.timer_active:
                self.timer_def()

            # animate lightbulbs
            if self.colorgame_anim:
                self.animation()

            # activate main game/randomization
            if self.colorgame:
                self.play()

            # reset values
            if self.reset:
                self.plyr_refund = False
                self.reset_values()
            else:
                self.plyr_refund = True
            
            # display end game screen
            if self.winner_isActive:
                self.blitwin()

            # displays menu for going back to main menu if true
            if self.menu_isActive:
                menu_state = self.menu_display.display(self.surface)
                # continue the game if resume
                # activate loadscreen quit if quit
                if menu_state == 'resume':
                    self.btn_state = True
                    self.btn_state_menu = True
                    self.btn_update = True
                    self.menu_isActive = False
                elif menu_state == 'quit':
                    music.Music.ingame_music1.stop()
                    self.loadscreen_quit = True

            # display loadscreen before going back to main menu
            if self.loadscreen_quit:
                if self.loading_quit.load(150, self.surface):
                    self.menu_isActive = False
                    self.return_value = 'main_menu'
                    self.loadscreen_quit = False

        # returns the return_value for the state of the game
        return self.return_value

    # update button array and initialization
    def updatebuttons(self):
        self.btn_red_array = [self.ui_rect.left + (self.btn_dimen[1]/2) + self.ui_margin, self.ui_rect.centery - (12 * self.scale[1]), [self.btn_red_img, self.btn_red_active_img], self.scale[1], 1, 1]
        self.btn_green_array = [self.btn_red_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_green_img, self.btn_green_active_img], self.scale[1], 1, 1]
        self.btn_blue_array = [self.btn_green_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_blue_img, self.btn_blue_active_img], self.scale[1], 1, 1]
        self.btn_pink_array = [self.btn_blue_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_pink_img, self.btn_pink_active_img], self.scale[1], 1, 1]
        self.btn_yellow_array = [self.btn_pink_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_yellow_img, self.btn_yellow_active_img], self.scale[1], 1, 1]
        self.btn_violet_array = [self.btn_yellow_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_violet_img, self.btn_violet_active_img], self.scale[1], 1, 1]
        self.btn_bet_array = [self.ui_rect.right - ((96 * self.scale[1]/2) + self.ui_margin), self.ui_rect.centery - (16 * self.scale[1]), [self.btn_bet_img, self.btn_bet_active_img], self.scale[1], 1.05, 1]
        self.btn_menu_array = [self.ui_rect.left + ((self.btn_menu_img.get_width()/2 * self.scale[1]) + (8 * self.scale[1])), self.ui_rect.top - ((self.btn_menu_img.get_height()/2 * self.scale[1]) + (2 * self.scale[1])), [self.btn_menu_img, self.btn_menu_active_img], self.scale[1], 1, 1]
        self.btn_red = btn.ButtonController(self.btn_red_array)
        self.btn_green = btn.ButtonController(self.btn_green_array)
        self.btn_blue = btn.ButtonController(self.btn_blue_array)
        self.btn_pink = btn.ButtonController(self.btn_pink_array)
        self.btn_yellow = btn.ButtonController(self.btn_yellow_array)
        self.btn_violet = btn.ButtonController(self.btn_violet_array)
        self.btn_bet = btn.ButtonController(self.btn_bet_array)
        self.btn_menu = btn.ButtonController(self.btn_menu_array)

    # function for the round indicator animation at the beginning of every round
    def round_display(self):
        # display all necessary assets(text) for round display
        self.round_surface.set_alpha(self.round_surface_alpha)
        self.surface.blit(self.round_surface, (0, 0))
        self.surface.blit(self.round_shadow_display, (self.round_x, self.round_y + (5 * (self.scale[1] * 2))))
        self.surface.blit(self.round_count_display, (self.round_x, self.round_y))

        # if self.round_state is fadebg, increase alpha value of bg
        # if self.round_state is slidein, slide text through the window
        # if self.round_state is unfadebg, decrease alpha value of bg, 
        # activate timer, and set round_start to False
        if self.round_state == 'fadebg':
            if self.round_surface_alpha <= 200:
                self.round_surface_alpha += 10
            else:
                self.round_state = 'slidein'
        elif self.round_state == 'slidein':
            if self.round_x < self.surfacex:
                if self.surfacex > self.surfacey:
                    self.round_x += 15 
                else:
                    self.round_x += 10
            else:
                self.round_state = 'unfadebg'      
        elif self.round_state == 'unfadebg':
            if self.round_surface_alpha > 0:
                self.round_surface_alpha -= 10
            else:
                if self.timer_active_delay.delay(1, 30):
                    self.btn_state = True
                    if not self.colorgame_anim and not self.colorgame and not self.reset:
                        self.timer_active = True
                        self.round_surface_alpha = 0
                        self.round_start = False

    # resets values for the round_display function
    def round_reset(self):
        self.round_start = True
        self.round_state = 'fadebg'

    # updates the text of the round indicator animation
    def round_text_update(self):
        self.round_count_render = self.font_round.render("ROUND " + (str(self.round_count)), False, self.maintxt_clr)
        self.round_shadow_render = self.font_round.render("ROUND " + (str(self.round_count)), False, self.shadow_clr)
        self.round_count_display = pygame.transform.scale(self.round_count_render, (self.round_count_render.get_width() * (self.scale[1] * 2), self.round_count_render.get_height() * (self.scale[1] * 2)))
        self.round_shadow_display = pygame.transform.scale(self.round_shadow_render, (self.round_shadow_render.get_width() * (self.scale[1] * 2), self.round_shadow_render.get_height() * (self.scale[1] * 2)))

    # resets the x position of the round indicator animation for next round
    def round_text_x_reset(self):
        self.round_x = 0 - (self.round_count_display.get_width() + (40 * self.scale[1]))

    # timer for the game
    def timer_def(self):
        # if self.timer_value is greater than 0, decrease it to one 
        # if not, check if self.plyr_choice is not empty, if it is
        # decrease self.plyr_balance by half of the value of self.bet_val,
        # reset self.timer_value, and set self.colorgame_anim to True
        if self.timer_value > 0:
            if self.timer_delay.delay(1, 60):
                self.timer_value -= 1
                self.timer_delay.reset()
        else:
            self.btn_state = False
            if self.plyr_choice == []:
                self.plyr_bal -= int(self.bet_val/2)
            self.enemybot_bet()
            self.colorgame_anim = True
            self.timer_value = self.timer_default_value
            self.timer_active = False

    # enemybot ai
    def enemybot_bet(self):
        # first calculate the possible max number of bets of enemybot
        self.enemybot_max_bet = int(self.enemybot_bal/self.bet_val)

        # if the quotient is greater than 6, set 6 as the value of self.enemybot_max_bet
        # if not, retain value of self.enemybot_max_bet
        if self.enemybot_max_bet > 6:
            self.enemybot_max_bet = 6
        else:
            self.enemybot_max_bet = self.enemybot_max_bet

        # determines the bet count of enemybot using random.randint
        self.enemybot_betcount = random.randint(1, self.enemybot_max_bet)

        # For loop for getting the colors for the enemybot append those colors to
        # self.enemybot_bet_clr, and decrease value of self.enemybot_bal depending
        # on value of self.bet_val.
        for i in range(self.enemybot_betcount):
            self.enemybot_bet_clr = self.colors[random.randint(1, 6)]
            if self.enemybot_bet_clr not in self.enemybot_choice:
                self.enemybot_bal -= self.bet_val
                self.enemybot_choice.append(self.enemybot_bet_clr)

    # animation for the lightbulbs before color game
    def animation(self):
        # if statement for repitions of the animation
        # if true, animate the lightbulbs
        # if false, set all the colors to default color, reset counters, set self.colorgame to True, and set self.colorgame_anim to False
        if self.colorgame_anim_ctr1 < 12:
            # if self.colorgame_anim_state is update, change colors depending on value of self.colorgame_anim_ctr2
            # if self.colorgame_anim_state is delay, delay the color change of the animation
            # if self.colorgame_anim_state is reset, add one to both counters and set self.colorgame_anim_state to update
            if self.colorgame_anim_state == 'update':
                # if self.colorgame_anim_ctr2 is less than 4, set color to lightbulbs, if not, set self.colorgame_anim_ctr2 to 0
                if self.colorgame_anim_ctr2 < 4:
                    # if self.colorgame_anim_ctr2 is 0, set all colors to default color
                    # if self.colorgame_anim_ctr2 is 1, set second and third color to default color
                    # if self.colorgame_anim_ctr2 is 2, set first and third color to default color
                    # if self.colorgame_anim_ctr2 is 0, set first and second color to default color
                    if self.colorgame_anim_ctr2 == 0:
                        self.final_result = [0, 0, 0]
                    elif self.colorgame_anim_ctr2 == 1:
                        self.final_result[1], self.final_result[2] = 0, 0
                    elif self.colorgame_anim_ctr2 == 2:
                        self.final_result[0], self.final_result[2] = 0, 0
                    elif self.colorgame_anim_ctr2 == 3:
                        self.final_result[0], self.final_result[1] = 0, 0

                    # If self.colorgame_anim_ctr2 not equal to 0, get a random color 
                    # and store it temporarily to self.final_result.   
                    if self.colorgame_anim_ctr2 != 0:
                        music.Music.randomizer.play()
                        self.final_result[self.colorgame_anim_ctr2 - 1] = random.randint(1, 6)
                    
                    # set self.colorgame_anim_state to delay
                    self.colorgame_anim_state = 'delay'
                else:
                    self.colorgame_anim_ctr2 = 0
            elif self.colorgame_anim_state == 'delay':
                if self.colorgame_delay.delay(1, 12):
                    self.colorgame_delay.reset()
                    self.colorgame_anim_state = 'reset'
            elif self.colorgame_anim_state == 'reset':
                self.colorgame_anim_ctr1 += 1
                self.colorgame_anim_ctr2 += 1
                self.colorgame_anim_state = 'update'
        else:
            self.final_result = [0, 0, 0]
            if self.colorgame_delay.delay(1, 32):
                self.colorgame_delay.reset()
                self.colorgame_anim_ctr1 = 0
                self.colorgame_anim_ctr2 = 0
                self.colorgame = True
                self.colorgame_anim = False

    # function for getting the results and checking if each player has chosen those results
    def play(self):
        # For loop for getting the three random colors for the
        # result and appending those colors to self.temp_result.
        for i in range(3):
            self.result_randomize = random.randint(1, 6)
            self.result_str.append(self.colors[(self.result_randomize)])
            self.temp_result.append(self.result_randomize)
        
        # store values of self.temp_result to self.final_result
        self.final_result = self.temp_result

        # check if colors from self.final_result is in array self.plyr_choice
        for i in self.plyr_choice:
            if i in self.result_str:
                self.plyr_bal += self.bet_val * 2
                self.plyr_displayadd += self.bet_val * 2

        # check if colors from self.final_result is in array self.enemybot_choice
        for i in self.enemybot_choice:
            if i in self.result_str:
                self.enemybot_bal += self.bet_val * 2
                self.enemybot_displayadd += self.bet_val * 2

        # play randomizer done sound
        if self.plyr_displayadd != 0:
            music.Music.randomizer_done1.play()
        else:
            music.Music.randomizer_done2.play()

        # set self.displayadd and self.reset to True, and set self.colorgame to False
        self.displayadd = True
        self.reset = True
        self.colorgame = False

    # resets the values of all necessary variables
    def reset_values(self):
        if self.reset_delay.delay(1, 50):
            self.btn_red.button2reset(self.surface)
            self.btn_green.button2reset(self.surface)
            self.btn_blue.button2reset(self.surface)
            self.btn_pink.button2reset(self.surface)
            self.btn_yellow.button2reset(self.surface)
            self.btn_violet.button2reset(self.surface)
            self.displayadd = False
            self.bet_val *= 2
            self.checkwin()
            if self.winner == None:
                self.plyr_displayadd = 0
                self.enemybot_displayadd = 0
                self.result_str = []
                self.temp_result = []
                self.enemybot_choice = []
                self.reset_delay.reset()
                self.round_count += 1
                self.round_text_update()
                self.round_text_x_reset()
                self.round_reset()
                self.timer_active_delay.reset()
            self.reset = False

    # checks if there is a winner
    def checkwin(self):
        # If both self.plyr_bal and self.enemybot_bal is less than self.bet_val,
        # check which of the two is greater than the other to determine the winner.
        
        # If not, check if either self.plyr_bal or self.enemybot_bal is less than
        # self.bet_val to determine which would be the winner
        if self.plyr_bal < self.bet_val and self.enemybot_bal < self.bet_val:
            if self.plyr_bal > self.enemybot_bal:
                self.winner = 'YOU WON'
            elif self.plyr_bal < self.enemybot_bal:
                self.winner = 'YOU LOST'
            elif self.plyr_bal == self.enemybot_bal:
                self.winner = 'DRAW'
        else:
            if self.plyr_bal < self.bet_val:
                self.winner = 'YOU LOST'
            elif self.enemybot_bal < self.bet_val:
                self.winner = 'YOU WON'
        
        # check if self.winner value is not None, if true, call function updatewin()
        # and set self.winner_isActive to True
        if self.winner != None:
            self.updatewin()
            self.winner_isActive = True

    # update the text for whether the player wins/loses
    def updatewin(self):
        music.Music.ingame_music1.stop()
        if self.winner == 'YOU WON':
            music.Music.victory_music.play()
        elif self.winner == 'YOU LOST' or self.winner == 'DRAW':
            music.Music.lose_music.play()
        self.winner_text_render = self.font_round.render(self.winner, False, self.maintxt_clr)
        self.winner_shadow_render = self.font_round.render(self.winner, False, self.shadow_clr)
        self.winner_text = pygame.transform.scale(self.winner_text_render, (self.winner_text_render.get_width() * self.scale[1] * 2, self.winner_text_render.get_height() * (self.scale[1] * 2)))
        self.winnder_shadow = pygame.transform.scale(self.winner_shadow_render, (self.winner_shadow_render.get_width() * self.scale[1] * 2, self.winner_shadow_render.get_height() * (self.scale[1] * 2)))
        self.winner_text_x, self.winner_text_y = self.surfacex/2 - self.winner_text.get_width()/2, 0 - self.winner_text.get_height()
        self.winner_text_y_center = self.surfacey/3 - self.winner_text.get_height()/2
        self.winner_anim = anim.SlideAnimation(self.winner_text_y)

    # displays the whether the player wins or loses
    def blitwin(self):
        # display bg 
        self.winner_bg.set_alpha(self.winner_bg_alpha)
        self.surface.blit(self.winner_bg, (0, 0))

        # display winner
        self.surface.blit(self.winnder_shadow, (self.winner_text_x, self.winner_text_y + (5 * (self.scale[1] * 2))))
        self.surface.blit(self.winner_text, (self.winner_text_x, self.winner_text_y))

        # if self.winner_state is fadefrom, set self.winner_bg_alpha to a certain value
        # if self.winner_state is displaywin, change self.winner_text_y up until a certain value is met
        # if self.winner_state is displaymes, display text message indicating to click anywhere to continue
        # and if left mouse button is clicked during that time, set self.loadscreen_quit to True
        if self.winner_state == 'fadefrom':
            if self.winner_bg_alpha <= 200:
                self.winner_bg_alpha += 10
            else:
                self.winner_state = 'displaywin'
        elif self.winner_state == 'displaywin':
            if self.winner_text_y < self.winner_text_y_center:
                self.winner_text_y = self.winner_anim.slide('right', 0.5)
            else:
                self.winner_state = 'displaymes'
        elif self.winner_state == 'displaymes':
            if self.winner_displaymes_delay.delay(1, 64):
                self.winner_displaymes.set_alpha(self.winner_displaymes_anim.fadeinout(0, 255, 0.03))
                self.winner_displaymes_shadow.set_alpha(self.winner_displaymes_anim.fadeinout(0, 255, 0.03))
                self.surface.blit(self.winner_displaymes_shadow, (self.surfacex/2 - self.winner_displaymes_shadow.get_width()/2, (self.surfacey/1.5 - self.winner_displaymes_shadow.get_height()/2) + (3 * self.scale[1])))
                self.surface.blit(self.winner_displaymes, (self.surfacex/2 - self.winner_displaymes.get_width()/2, self.surfacey/1.5 - self.winner_displaymes.get_height()/2))
                if pygame.mouse.get_pressed()[0]:
                    if self.winner == 'YOU WON':
                        music.Music.victory_music.stop()
                    elif self.winner == 'YOU LOST' or self.winner == 'DRAW':
                        music.Music.lose_music.stop()
                    self.loadscreen_quit = True

    # resets all necessary values for the next game
    def hard_reset(self):
        self.loading.reset()
        self.loading_quit.reset()
        self.fadefrom.reset()
        self.fadefrom_active = True
        self.initial_anim = True
        self.bal_ui1_rect.topleft = (0 - self.bal_ui1.get_width(), 0)
        self.bal_ui2_rect.topright = (self.surfacex + self.bal_ui2.get_width(), 0)
        self.ui_rect.topleft = (self.surfacex/2 - self.ui.get_width()/2, self.surfacey + (120 * self.scale[1]))
        self.updatebuttons()
        self.round_surface_alpha = 0
        self.btn_state_menu = False
        self.btn_update = True
        self.btn_red.button2reset(self.surface)
        self.btn_green.button2reset(self.surface)
        self.btn_blue.button2reset(self.surface)
        self.btn_pink.button2reset(self.surface)
        self.btn_yellow.button2reset(self.surface)
        self.btn_violet.button2reset(self.surface)
        self.colorgame_anim = False
        self.colorgame = False
        self.reset = False 
        self.colorgame_anim_state = 'update'
        self.colorgame_anim_ctr1 = 0
        self.colorgame_anim_ctr2 = 0
        self.plyr_bal = 1000
        self.enemybot_bal = 1000
        self.plyr_displayadd = 0
        self.enemybot_displayadd = 0
        self.result_str = []
        self.temp_result = []
        self.final_result = [0, 0, 0]
        self.enemybot_choice = []
        self.bet_val = 10
        self.round_count = 1
        self.round_start = False
        self.round_state = 'fadebg'
        self.round_text_update()
        self.round_text_x_reset()
        self.timer_active_delay.reset()
        self.reset_delay.reset()
        self.timer_active = False
        self.timer_value = self.timer_default_value
        self.return_value = 'gm1'
        self.winner = None
        self.updatewin()
        self.winner_isActive = False
        self.winner_bg_alpha = 0
        self.winner_state = 'fadefrom'
        self.winner_anim.reset_param()
        self.winner_displaymes_anim.reset()
        self.winner_displaymes_delay.reset()

class PvP():
    def __init__(self, surfacex:int, surfacey:int, surface:tuple):
        # window variables
        self.surface = surface
        self.surfacex, self.surfacey = surfacex, surfacey

        # load the img assets
        self.bg_img = pygame.image.load("assets/imgs/maingame/game_bg.png").convert_alpha()
        self.bal_ui_img1 = pygame.image.load("assets/imgs/maingame/balance/game_player1balance.png").convert_alpha()
        self.bal_ui_img2 = pygame.image.load("assets/imgs/maingame/balance/game_player2balance.png").convert_alpha()
        self.plyr_1_img = pygame.image.load("assets/imgs/maingame/player/game_player1.png").convert_alpha()
        self.plyr_2_img = pygame.image.load("assets/imgs/maingame/player/game_player2.png").convert_alpha()
        self.table_img = pygame.image.load("assets/imgs/maingame/game_table.png").convert_alpha()
        self.rndmizer_img = pygame.image.load("assets/imgs/maingame/game_randomizer.png").convert_alpha()
        self.ui_img = pygame.image.load("assets/imgs/maingame/game_ui1.png").convert_alpha()
        self.betcontainer_ui1_img = pygame.image.load("assets/imgs/maingame/bet_container/game_player1betcontainer.png")
        self.betcontainer_ui2_img = pygame.image.load("assets/imgs/maingame/bet_container/game_player2betcontainer.png")

        # resize the assets
        self.scale = surfacex/self.bg_img.get_width(), surfacey/self.bg_img.get_height()
        self.bg = pygame.transform.scale(self.bg_img, (self.bg_img.get_width() * self.scale[0], self.bg_img.get_height() * self.scale[1]))
        self.bal_ui1 = pygame.transform.scale(self.bal_ui_img1, (self.bal_ui_img1.get_width() * self.scale[0], self.bal_ui_img1.get_height() * self.scale[1]))
        self.bal_ui2 = pygame.transform.scale(self.bal_ui_img2, (self.bal_ui_img2.get_width() * self.scale[0], self.bal_ui_img2.get_height() * self.scale[1]))
        self.plyr_1 = pygame.transform.scale(self.plyr_1_img, (self.plyr_1_img.get_width() * self.scale[1], self.plyr_1_img.get_height() * self.scale[1]))
        self.plyr_2 = pygame.transform.scale(self.plyr_2_img, (self.plyr_2_img.get_width() * self.scale[1], self.plyr_2_img.get_height() * self.scale[1]))
        self.table = pygame.transform.scale(self.table_img, (self.table_img.get_width() * self.scale[0], self.table_img.get_height() * self.scale[1]))
        self.rndmizer = pygame.transform.scale(self.rndmizer_img, (self.rndmizer_img.get_width() * self.scale[1], self.rndmizer_img.get_height() * self.scale[1]))
        self.ui = pygame.transform.scale(self.ui_img, (self.ui_img.get_width() * self.scale[1], self.ui_img.get_height() * self.scale[1]))
        self.betcontainer_ui1 = pygame.transform.scale(self.betcontainer_ui1_img, (self.betcontainer_ui1_img.get_width() * self.scale[1], self.betcontainer_ui1_img.get_height() * self.scale[1]))
        self.betcontainer_ui2 = pygame.transform.scale(self.betcontainer_ui2_img, (self.betcontainer_ui2_img.get_width() * self.scale[1], self.betcontainer_ui2_img.get_height() * self.scale[1]))

        # plyr asset variables
        self.plyr_display = [self.plyr_1, self.plyr_2]
        self.plyr_betcontainer = [self.betcontainer_ui1, self.betcontainer_ui2]
        self.crrntplyr_counter = 0
        self.othrplyr_counter = 1
        self.temp_val = None

        # load other player color choices
        self.othrplyr_red_img = pygame.image.load("assets/imgs/maingame/enemy_choice/red.png").convert_alpha()
        self.othrplyr_green_img = pygame.image.load("assets/imgs/maingame/enemy_choice/green.png").convert_alpha()
        self.othrplyr_blue_img = pygame.image.load("assets/imgs/maingame/enemy_choice/blue.png").convert_alpha()
        self.othrplyr_pink_img = pygame.image.load("assets/imgs/maingame/enemy_choice/pink.png").convert_alpha()
        self.othrplyr_yellow_img = pygame.image.load("assets/imgs/maingame/enemy_choice/yellow.png").convert_alpha()
        self.othrplyr_violet_img = pygame.image.load("assets/imgs/maingame/enemy_choice/violet.png").convert_alpha()

        # resize othrplyr color choices
        self.othrplyr_red = pygame.transform.scale(self.othrplyr_red_img, (self.othrplyr_red_img.get_width() * self.scale[1], self.othrplyr_red_img.get_height() * self.scale[1]))
        self.othrplyr_green = pygame.transform.scale(self.othrplyr_green_img, (self.othrplyr_green_img.get_width() * self.scale[1], self.othrplyr_green_img.get_height() * self.scale[1]))
        self.othrplyr_blue = pygame.transform.scale(self.othrplyr_blue_img, (self.othrplyr_blue_img.get_width() * self.scale[1], self.othrplyr_blue_img.get_height() * self.scale[1]))
        self.othrplyr_pink = pygame.transform.scale(self.othrplyr_pink_img, (self.othrplyr_pink_img.get_width() * self.scale[1], self.othrplyr_pink_img.get_height() * self.scale[1]))
        self.othrplyr_yellow = pygame.transform.scale(self.othrplyr_yellow_img, (self.othrplyr_yellow_img.get_width() * self.scale[1], self.othrplyr_yellow_img.get_height() * self.scale[1]))
        self.othrplyr_violet = pygame.transform.scale(self.othrplyr_violet_img, (self.othrplyr_violet_img.get_width() * self.scale[1], self.othrplyr_violet_img.get_height() * self.scale[1]))

        # load lightbulb colors
        self.clr_default_img = pygame.image.load("assets/imgs/maingame/color_result/default.png").convert_alpha()
        self.clr_red_img = pygame.image.load("assets/imgs/maingame/color_result/red.png").convert_alpha()
        self.clr_green_img = pygame.image.load("assets/imgs/maingame/color_result/green.png").convert_alpha()
        self.clr_blue_img = pygame.image.load("assets/imgs/maingame/color_result/blue.png").convert_alpha()
        self.clr_pink_img = pygame.image.load("assets/imgs/maingame/color_result/pink.png").convert_alpha()
        self.clr_yellow_img = pygame.image.load("assets/imgs/maingame/color_result/yellow.png").convert_alpha()
        self.clr_violet_img = pygame.image.load("assets/imgs/maingame/color_result/violet.png").convert_alpha()

        # resize lightbulbs
        self.clr_default = pygame.transform.scale(self.clr_default_img, (self.clr_default_img.get_width() * self.scale[1], self.clr_default_img.get_height() * self.scale[1]))
        self.clr_red = pygame.transform.scale(self.clr_red_img, (self.clr_red_img.get_width() * self.scale[1], self.clr_red_img.get_height() * self.scale[1]))
        self.clr_green = pygame.transform.scale(self.clr_green_img, (self.clr_green_img.get_width() * self.scale[1], self.clr_green_img.get_height() * self.scale[1]))
        self.clr_blue = pygame.transform.scale(self.clr_blue_img, (self.clr_blue_img.get_width() * self.scale[1], self.clr_blue_img.get_height() * self.scale[1]))
        self.clr_pink = pygame.transform.scale(self.clr_pink_img, (self.clr_pink_img.get_width() * self.scale[1], self.clr_pink_img.get_height() * self.scale[1]))
        self.clr_yellow = pygame.transform.scale(self.clr_yellow_img, (self.clr_yellow_img.get_width() * self.scale[1], self.clr_yellow_img.get_height() * self.scale[1]))
        self.clr_violet = pygame.transform.scale(self.clr_violet_img, (self.clr_violet_img.get_width() * self.scale[1], self.clr_violet_img.get_height() * self.scale[1]))

        # array for all lightbulb colors
        self.clr_result = [self.clr_default, self.clr_red, self.clr_green, self.clr_blue, self.clr_pink, self.clr_yellow, self.clr_violet]
        
        # array for all colors
        self.colors = ['default', 'red', 'green', 'blue', 'pink', 'yellow', 'violet']

        # asset rect x and y position
        # othrplyr rect values
        self.othrplyr_rect = self.plyr_display[self.othrplyr_counter].get_rect()
        self.othrplyr_rect.topleft = (self.surfacex/2 - self.plyr_display[self.othrplyr_counter].get_width()/2, (self.surfacey/2 - (self.plyr_display[self.othrplyr_counter].get_height()/2) + (40 * self.scale[1])))

        # randomizer rect values
        self.rndmizer_rect = self.rndmizer.get_rect()
        self.rndmizer_rect.topleft = (self.surfacex/2 - self.rndmizer.get_width()/2, (self.surfacey/2) + (50 * self.scale[1]))
        
        # balance ui rect values
        self.bal_ui1_rect = self.bal_ui1.get_rect()
        self.bal_ui1_rect.topleft = (0 - self.bal_ui1.get_width(), 0)
        self.bal_ui1_finalleft = 0
        self.bal_ui2_rect = self.bal_ui2.get_rect()
        self.bal_ui2_rect.topright = (self.surfacex + self.bal_ui2.get_width(), 0)
        self.bal_ui2_finalright = self.surfacex
        
        # crrntplyr ui rect values
        self.ui_rect = self.ui.get_rect()
        self.ui_rect.topleft = (self.surfacex/2 - self.ui.get_width()/2, self.surfacey + (120 * self.scale[1]))
        
        # othrplyr bet container rect values
        self.othrplyr_betcontainer_rect = self.plyr_betcontainer[self.othrplyr_counter].get_rect()
        self.othrplyr_betcontainer_y = self.othrplyr_rect.top - (self.plyr_betcontainer[self.othrplyr_counter].get_height() + (16 * self.scale[1]))
        self.othrplyr_betcontainer_rect.topleft = self.surfacex/2 - self.plyr_betcontainer[self.othrplyr_counter].get_width()/2, self.othrplyr_betcontainer_y

        # amount of space between othrplyr choices
        self.othrplyr_space = (4 * self.scale[1])

        # othrplyr choice x and y
        self.othrplyr_blue_x = (self.surfacex/2 - self.othrplyr_blue.get_width()/2) - ((self.othrplyr_blue.get_width()/2) + self.othrplyr_space)
        self.othrplyr_green_x = self.othrplyr_blue_x - (self.othrplyr_green.get_width() + self.othrplyr_space * 2)
        self.othrplyr_red_x = self.othrplyr_green_x - (self.othrplyr_red.get_width() + self.othrplyr_space * 2)
        self.othrplyr_pink_x = (self.surfacex/2 - self.othrplyr_pink.get_width()/2) + ((self.othrplyr_pink.get_width()/2) + self.othrplyr_space)
        self.othrplyr_yellow_x = self.othrplyr_pink_x + (self.othrplyr_yellow.get_width() + self.othrplyr_space * 2)
        self.othrplyr_violet_x = self.othrplyr_yellow_x + (self.othrplyr_violet.get_width() + self.othrplyr_space * 2)

        # load button assets
        self.btn_red_img = pygame.image.load("assets/imgs/maingame/button/red.png").convert_alpha()
        self.btn_red_active_img = pygame.image.load("assets/imgs/maingame/button_active/red.png").convert_alpha()

        self.btn_green_img = pygame.image.load("assets/imgs/maingame/button/green.png").convert_alpha()
        self.btn_green_active_img = pygame.image.load("assets/imgs/maingame/button_active/green.png").convert_alpha()

        self.btn_blue_img = pygame.image.load("assets/imgs/maingame/button/blue.png").convert_alpha()
        self.btn_blue_active_img = pygame.image.load("assets/imgs/maingame/button_active/blue.png").convert_alpha()

        self.btn_pink_img = pygame.image.load("assets/imgs/maingame/button/pink.png").convert_alpha()
        self.btn_pink_active_img = pygame.image.load("assets/imgs/maingame/button_active/pink.png").convert_alpha()

        self.btn_yellow_img = pygame.image.load("assets/imgs/maingame/button/yellow.png").convert_alpha()
        self.btn_yellow_active_img = pygame.image.load("assets/imgs/maingame/button_active/yellow.png").convert_alpha()

        self.btn_violet_img = pygame.image.load("assets/imgs/maingame/button/violet.png").convert_alpha()
        self.btn_violet_active_img = pygame.image.load("assets/imgs/maingame/button_active/violet.png").convert_alpha()

        self.btn_bet_img = pygame.image.load("assets/imgs/maingame/button/bet.png").convert_alpha()
        self.btn_bet_active_img = pygame.image.load("assets/imgs/maingame/button_active/bet.png").convert_alpha()

        self.btn_menu_img = pygame.image.load("assets/imgs/maingame/menu_button/menu1.png").convert_alpha()
        self.btn_menu_active_img = pygame.image.load("assets/imgs/maingame/menu_button/menu2.png").convert_alpha()

        # button additional position values
        self.ui_margin = (48 * self.scale[1])
        self.btn_dimen = (48 * self.scale[1], 48 * self.scale[1])
        self.btn_space = 25 * self.scale[1]

        # button arrays
        # button array for color choices
        self.btn_red_array = [self.ui_rect.left + (self.btn_dimen[1]/2) + self.ui_margin, self.ui_rect.centery - (12 * self.scale[1]), [self.btn_red_img, self.btn_red_active_img], self.scale[1], 1, 1]
        self.btn_green_array = [self.btn_red_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_green_img, self.btn_green_active_img], self.scale[1], 1, 1]
        self.btn_blue_array = [self.btn_green_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_blue_img, self.btn_blue_active_img], self.scale[1], 1, 1]
        self.btn_pink_array = [self.btn_blue_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_pink_img, self.btn_pink_active_img], self.scale[1], 1, 1]
        self.btn_yellow_array = [self.btn_pink_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_yellow_img, self.btn_yellow_active_img], self.scale[1], 1, 1]
        self.btn_violet_array = [self.btn_yellow_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_violet_img, self.btn_violet_active_img], self.scale[1], 1, 1]

        # button array for bet button
        self.btn_bet_array = [self.ui_rect.right - ((96 * self.scale[1]/2) + self.ui_margin), self.ui_rect.centery - (16 * self.scale[1]), [self.btn_bet_img, self.btn_bet_active_img], self.scale[1], 1.05, 1]
        
        # button array for main menu button
        self.btn_menu_array = [self.ui_rect.left + ((self.btn_menu_img.get_width()/2 * self.scale[1]) + (8 * self.scale[1])), self.ui_rect.top - ((self.btn_menu_img.get_height()/2 * self.scale[1]) + (2 * self.scale[1])), [self.btn_menu_img, self.btn_menu_active_img], self.scale[1], 1, 1]

        # button initializtation
        self.btn_state = False
        self.btn_state_menu = False
        self.btn_update = True
        self.btn_red = btn.ButtonController(self.btn_red_array)
        self.btn_green = btn.ButtonController(self.btn_green_array)
        self.btn_blue = btn.ButtonController(self.btn_blue_array)
        self.btn_pink = btn.ButtonController(self.btn_pink_array)
        self.btn_yellow = btn.ButtonController(self.btn_yellow_array)
        self.btn_violet = btn.ButtonController(self.btn_violet_array)
        
        # bet button
        self.btn_bet = btn.ButtonController(self.btn_bet_array)

        # menu button
        self.btn_menu = btn.ButtonController(self.btn_menu_array)

        # font initialization
        self.font_round = pygame.font.FontType("assets/fonts/upheavtt.ttf", 64)
        self.font_round_small = pygame.font.FontType("assets/fonts/upheavtt.ttf", 32)
        self.font_timer = pygame.font.FontType("assets/fonts/upheavtt.ttf", 64)
        self.font_num = pygame.font.FontType("assets/fonts/balance_font.ttf", 32)
        
        # text balance colors
        self.clr_balance_green = (57, 255, 20)
        self.clr_balance_red = (255, 49, 49)
        
        # initial colors for balances
        self.clr_balance1 = self.clr_balance_green
        self.clr_balance2 = self.clr_balance_green

        # loading screen
        self.loading = load.Loading(self.surfacex, self.surfacey)
        self.loading_quit = load.Loading(self.surfacex, self.surfacey)
        
        # bool var responsible for activating loadscreen before going back to main menu
        self.loadscreen_quit = False

        # fade in animation at start
        self.fadefrom_active = True
        self.fadefrom = anim.FadeFrom(self.surfacex, self.surfacey)

        # initial animation
        self.initial_anim = True

        # bet container animation
        self.othrplyr_betcontainer_anim = anim.HoverAnimation()

        # text color values
        self.maintxt_clr = (255, 255, 255)
        self.shadow_clr = (1, 59, 96)

        # variables for displaying the round count each round
        # initialization of delay before round start
        self.round_delay = dly.Delay()
        
        # bool var responsible of animating the round count
        self.round_start = False
        
        # initial state of the animation
        self.round_state = 'fadebg'
        
        # bg of the animation
        self.round_surface = pygame.Surface((self.surfacex, self.surfacey))
        self.round_surface.fill((0, 0, 0))
        
        # initial alpha value of the bg
        self.round_surface_alpha = 0
        
        # variable that holds the round count
        self.round_count = 1
        
        # renders the necessary round text to be displayed on the screen
        self.round_count_render = self.font_round.render("ROUND " + (str(self.round_count)), False, self.maintxt_clr)
        self.round_shadow_render = self.font_round.render("ROUND " + (str(self.round_count)), False, self.shadow_clr)
        
        # resizes the round text 
        self.round_count_display = pygame.transform.scale(self.round_count_render, (self.round_count_render.get_width() * (self.scale[1] * 2), self.round_count_render.get_height() * (self.scale[1] * 2)))
        self.round_shadow_display = pygame.transform.scale(self.round_shadow_render, (self.round_shadow_render.get_width() * (self.scale[1] * 2), self.round_shadow_render.get_height() * (self.scale[1] * 2)))
        
        # rect, and xy values of the round count
        self.round_x = 0 - (self.round_count_display.get_width() + (40 * self.scale[1]))
        self.round_y = self.surfacey/2 - self.round_count_display.get_height()
        self.round_count_rect = self.round_count_display.get_rect()
        self.round_count_rect.topleft = (self.round_x, self.round_y)

        # timer variables
        # initializes delay before timer becomes active
        self.timer_active_delay = dly.Delay()
        
        # bool var responsible of activating timer
        self.timer_active = False
        
        # timer values
        self.timer_default_value = 30
        self.timer_value = self.timer_default_value
        
        # initializes delay for each decrease of timer value
        self.timer_delay = dly.Delay()

        # bet value
        self.bet_val = 10

        # player 1 and 2 balance variable
        self.plyr_bal = [1000, 1000]

        # array that keeps player 1 and 2 choice
        self.plyr_choice = [[], []]
        
        # if true, refunds the player's balance if unclicking a button
        self.plyr_refund = True

        # bet click counter for swapping of players
        self.bet_click = 0

        # colorgame variables
        # bool var responsible for starting the randomization of colors
        self.colorgame = False

        # bool var responsible for animating assets for randomization of colors
        self.colorgame_anim = False
        
        # counters used for the animations 
        self.colorgame_anim_ctr1 = 0
        self.colorgame_anim_ctr2 = 0

        # initial state of the colorgame animation
        self.colorgame_anim_state = 'update'
        
        # delays each color appearance in the animation
        self.colorgame_delay = dly.Delay()

        # win amount display
        # bool var responsible for displaying add in the balance
        self.displayadd = False

        # display add values
        self.plyr_displayadd = [0, 0]

        # result variables
        self.result_randomize = None
        self.result_str = []
        self.temp_result = []

        # initial values for final result
        self.final_result = [0, 0, 0]

        # partial reset variables
        self.reset = False
        self.reset_delay = dly.Delay()

        # variables for displaying winner
        # variable of winner
        self.winner = None

        # bool var resposible of displaying winner 
        self.winner_isActive = False

        # initial state of display animation of winner
        self.winner_state = 'fadefrom'

        # bg of winner display
        self.winner_bg = pygame.Surface((self.surfacex, self.surfacey))
        
        # initial alpha value of bg of winner display
        self.winner_bg_alpha = 0

        # initialization of delay for displaying message after displaying winner
        self.winner_displaymes_delay = dly.Delay()

        # text render for the message after displaying winner
        self.winner_displaymes_render = self.font_round_small.render('CLICK ANYWHERE TO CONTINUE', False, self.maintxt_clr)
        self.winner_displaymes_shadow_render = self.font_round_small.render('CLICK ANYWHERE TO CONTINUE', False, self.shadow_clr)
        
        # resize text render for the message
        self.winner_displaymes = pygame.transform.scale(self.winner_displaymes_render, (self.winner_displaymes_render.get_width() * self.scale[1], self.winner_displaymes_render.get_height() * self.scale[1]))
        self.winner_displaymes_shadow = pygame.transform.scale(self.winner_displaymes_shadow_render, (self.winner_displaymes_shadow_render.get_width() * self.scale[1], self.winner_displaymes_shadow_render.get_height() * self.scale[1]))
        self.winner_displaymes_anim = anim.FadeInOut()

        # main menu variables
        # bool var responsible for displaying menu
        self.menu_isActive = False
        self.menu_display = mm.MainMenuQuit('Your progress won\'t be saved.', pygame.image.load("assets/imgs/mainmenu/mainmenu_quit2.png"), self.surfacex, self.surfacey, 1.7)

        # state variable of the game
        self.return_value = 'gm2'

    def display(self):
        # loadscreen before game start
        if self.loading.load(150, self.surface):
            # display the background assets
            self.surface.blit(self.bg, (0, 0))
            self.surface.blit(self.bal_ui1, (self.bal_ui1_rect.x, self.bal_ui1_rect.y))
            self.surface.blit(self.bal_ui2, (self.bal_ui2_rect.x, self.bal_ui2_rect.y))
            
            # display player 1 or 2 asset 
            self.surface.blit(self.plyr_display[self.othrplyr_counter], (self.othrplyr_rect.x, self.othrplyr_rect.y))
            
            # display table
            self.surface.blit(self.table, (0, self.surfacey - (self.table.get_height() - (20 * self.scale[1]))))
            
            # display color randomizer
            self.surface.blit(self.rndmizer, (self.rndmizer_rect.x, self.rndmizer_rect.y))
        
            # display result colors
            self.surface.blit(self.clr_result[self.final_result[0]], ((self.surfacex/2 - self.clr_result[0].get_width()/2) - ((20 * self.scale[1]) + (self.clr_result[0].get_width())), (self.rndmizer_rect.top + (7.5 * self.scale[1])) - self.clr_result[0].get_height()))
            self.surface.blit(self.clr_result[self.final_result[1]], (self.surfacex/2 - self.clr_result[0].get_width()/2, (self.rndmizer_rect.top + (7.5 * self.scale[1])) - self.clr_result[0].get_height()))
            self.surface.blit(self.clr_result[self.final_result[2]], ((self.surfacex/2 - self.clr_result[0].get_width()/2) + ((20 * self.scale[1]) + (self.clr_result[0].get_width())), (self.rndmizer_rect.top + (7.5 * self.scale[1])) - self.clr_result[0].get_height()))

            # display player ui (button container)
            self.surface.blit(self.ui, (self.ui_rect.x, self.ui_rect.y))

            # display buttons
            red_bet = self.btn_red.button2(self.surface, self.btn_update, self.btn_state)
            green_bet = self.btn_green.button2(self.surface, self.btn_update, self.btn_state)
            blue_bet = self.btn_blue.button2(self.surface, self.btn_update, self.btn_state)
            pink_bet = self.btn_pink.button2(self.surface, self.btn_update, self.btn_state)
            yellow_bet = self.btn_yellow.button2(self.surface, self.btn_update, self.btn_state)
            violet_bet = self.btn_violet.button2(self.surface, self.btn_update, self.btn_state)

            # display othrplyr bet
            # othrplyr_betcontainer animation
            self.othrplyr_betcontainer_rect.y = self.othrplyr_betcontainer_anim.hover(self.othrplyr_betcontainer_y, 4, 0.06)

            # displays the bet container 
            self.surface.blit(self.plyr_betcontainer[self.othrplyr_counter], (self.othrplyr_betcontainer_rect.x, self.othrplyr_betcontainer_rect.y))
            
            # check if self.plyr_choice is not empty and if true, display colors in self.plyr_choice
            if self.plyr_choice[self.othrplyr_counter] != []:
                if 'red' in self.plyr_choice[self.othrplyr_counter]:
                    self.surface.blit(self.othrplyr_red, (self.othrplyr_red_x, self.othrplyr_betcontainer_rect.y + (8 * self.scale[1])))
                if 'green' in self.plyr_choice[self.othrplyr_counter]:
                    self.surface.blit(self.othrplyr_green, (self.othrplyr_green_x, self.othrplyr_betcontainer_rect.y + (8 * self.scale[1])))
                if 'blue' in self.plyr_choice[self.othrplyr_counter]:
                    self.surface.blit(self.othrplyr_blue, (self.othrplyr_blue_x, self.othrplyr_betcontainer_rect.y + (8 * self.scale[1])))
                if 'pink' in self.plyr_choice[self.othrplyr_counter]:
                    self.surface.blit(self.othrplyr_pink, (self.othrplyr_pink_x, self.othrplyr_betcontainer_rect.y + (8 * self.scale[1])))
                if 'yellow' in self.plyr_choice[self.othrplyr_counter]:        
                    self.surface.blit(self.othrplyr_yellow, (self.othrplyr_yellow_x, self.othrplyr_betcontainer_rect.y + (8 * self.scale[1])))
                if 'violet' in self.plyr_choice[self.othrplyr_counter]:
                    self.surface.blit(self.othrplyr_violet, (self.othrplyr_violet_x, self.othrplyr_betcontainer_rect.y + (8 * self.scale[1])))

            # display timer
            self.timer_render = self.font_timer.render(str(self.timer_value), False, self.maintxt_clr)
            self.timer_shadow_render = self.font_timer.render(str(self.timer_value), False, self.shadow_clr)
            self.timer = pygame.transform.scale(self.timer_render, (self.timer_render.get_width() * self.scale[1], self.timer_render.get_height() * self.scale[1]))
            self.timer_shadow = pygame.transform.scale(self.timer_shadow_render, (self.timer_shadow_render.get_width() * self.scale[1], self.timer_shadow_render.get_height() * self.scale[1]))
            self.surface.blit(self.timer_shadow, (self.surfacex/2 - self.timer.get_width()/2, 17 * self.scale[1]))
            self.surface.blit(self.timer, (self.surfacex/2 - self.timer.get_width()/2, 12 * self.scale[1]))

            # display round count under timer
            self.round_small_render = self.font_round_small.render('ROUND ' + str(self.round_count), False, self.maintxt_clr)
            self.round_small_shadow = self.font_round_small.render('ROUND ' + str(self.round_count), False, self.shadow_clr)
            self.round_small_display = pygame.transform.scale(self.round_small_render, (self.round_small_render.get_width() * self.scale[1]/1.5, self.round_small_render.get_height() * self.scale[1]/1.5))
            self.round_small_shadow_display =  pygame.transform.scale(self.round_small_shadow, (self.round_small_shadow.get_width() * self.scale[1]/1.5, self.round_small_shadow.get_height() * self.scale[1]/1.5))
            self.surface.blit(self.round_small_shadow_display, (self.surfacex/2 - self.round_small_display.get_width()/2, 75 * self.scale[1] + (3 * self.scale[1]/1.5)))
            self.surface.blit(self.round_small_display, (self.surfacex/2 - self.round_small_display.get_width()/2, 75 * self.scale[1]))

            # display bet value
            self.bet_display_render = self.font_num.render(str(self.bet_val), False, self.clr_balance_green)
            self.bet_display = pygame.transform.scale(self.bet_display_render, (self.bet_display_render.get_width() * self.scale[1], self.bet_display_render.get_height() * self.scale[1]))
            self.surface.blit(self.bet_display, (self.rndmizer_rect.centerx - self.bet_display.get_width()/2, (self.rndmizer_rect.centery - self.bet_display.get_height()/2) - (20 * self.scale[1])))

            # display balance of player 1 and player 2
            if self.plyr_bal[0] >= self.bet_val:
                self.clr_balance1 = self.clr_balance_green
            else:
                self.clr_balance1 = self.clr_balance_red

            self.plyr_1_bal_render = self.font_num.render(str(self.plyr_bal[0]), False, self.clr_balance1)
            self.plyr_1_bal_display = pygame.transform.scale(self.plyr_1_bal_render, (self.plyr_1_bal_render.get_width() * self.scale[1], self.plyr_1_bal_render.get_height() * self.scale[1]))
            self.plyr_bal_uiy = self.bal_ui1_rect.bottom - (self.plyr_1_bal_display.get_height() + self.ui_margin/3)
            self.surface.blit(self.plyr_1_bal_display, (self.bal_ui1_rect.right - (self.plyr_1_bal_display.get_width() + self.ui_margin/2), self.plyr_bal_uiy))

            if self.plyr_bal[1] >= self.bet_val:
                self.clr_balance2 = self.clr_balance_green
            else:
                self.clr_balance2 = self.clr_balance_red

            self.plyr_2_bal_render = self.font_num.render(str(self.plyr_bal[1]), False, self.clr_balance2)
            self.plyr_2_bal_display = pygame.transform.scale(self.plyr_2_bal_render, (self.plyr_2_bal_render.get_width() * self.scale[1], self.plyr_2_bal_render.get_height() * self.scale[1]))
            self.surface.blit(self.plyr_2_bal_display, (self.bal_ui2_rect.right - (self.plyr_2_bal_display.get_width() + self.ui_margin/2), self.plyr_bal_uiy))

            # display balance add of both players after each round
            if self.displayadd:
                if self.plyr_displayadd[0] != 0:
                    self.plyr_1_displayadd_render = self.font_num.render('+' + str(self.plyr_displayadd[0]), False, self.clr_balance_green)
                    self.plyr_1_displayadd_display = pygame.transform.scale(self.plyr_1_displayadd_render, (self.plyr_1_displayadd_render.get_width() * self.scale[1], self.plyr_1_displayadd_render.get_height() * self.scale[1]))
                    self.surface.blit(self.plyr_1_displayadd_display, (self.bal_ui1_rect.left + self.ui_margin/2, self.plyr_bal_uiy))
                if self.plyr_displayadd[1] != 0:
                    self.plyr_2_displayadd_render = self.font_num.render('+' + str(self.plyr_displayadd[1]), False, self.clr_balance_green)
                    self.plyr_2_displayadd_display = pygame.transform.scale(self.plyr_2_displayadd_render, (self.plyr_2_displayadd_render.get_width() * self.scale[1], self.plyr_2_displayadd_render.get_height() * self.scale[1]))
                    self.surface.blit(self.plyr_2_displayadd_display, (self.bal_ui2_rect.left + self.ui_margin/2, self.plyr_bal_uiy))
            
            # Checks the color buttons pressed, if clicked while not activated, add color to array self.plyr_choice and
            # decrease self.plyr_bal depending on value of self.bet_val. If button is already activated and player decides
            # to click it, the certain color will be removed from self.plyr_choice and players balance will add depending on
            # value of self.bet_val

            # for red button
            if red_bet:
                if self.plyr_bal[self.crrntplyr_counter] >= self.bet_val:
                    if 'red' not in self.plyr_choice[self.crrntplyr_counter]:
                        self.plyr_choice[self.crrntplyr_counter].append('red')
                        self.plyr_bal[self.crrntplyr_counter] -= self.bet_val
                elif 'red' not in self.plyr_choice[self.crrntplyr_counter]:
                    self.btn_red.button2reset(self.surface)
            elif not red_bet and 'red' in self.plyr_choice[self.crrntplyr_counter]:
                self.plyr_choice[self.crrntplyr_counter].remove('red')
                if self.plyr_refund:
                    self.plyr_bal[self.crrntplyr_counter] += self.bet_val
            
            # for green button
            if green_bet:
                if self.plyr_bal[self.crrntplyr_counter] >= self.bet_val:
                    if 'green' not in self.plyr_choice[self.crrntplyr_counter]:
                        self.plyr_choice[self.crrntplyr_counter].append('green')
                        self.plyr_bal[self.crrntplyr_counter] -= self.bet_val
                elif 'green' not in self.plyr_choice[self.crrntplyr_counter]:
                    self.btn_green.button2reset(self.surface)
            elif not green_bet and 'green' in self.plyr_choice[self.crrntplyr_counter]:
                self.plyr_choice[self.crrntplyr_counter].remove('green')
                if self.plyr_refund:
                    self.plyr_bal[self.crrntplyr_counter] += self.bet_val
            
            # for blue button
            if blue_bet:
                if self.plyr_bal[self.crrntplyr_counter] >= self.bet_val:
                    if 'blue' not in self.plyr_choice[self.crrntplyr_counter]:
                        self.plyr_choice[self.crrntplyr_counter].append('blue')
                        self.plyr_bal[self.crrntplyr_counter] -= self.bet_val
                elif 'blue' not in self.plyr_choice[self.crrntplyr_counter]:
                    self.btn_blue.button2reset(self.surface)
            elif not blue_bet and 'blue' in self.plyr_choice[self.crrntplyr_counter]:
                self.plyr_choice[self.crrntplyr_counter].remove('blue')
                if self.plyr_refund:
                    self.plyr_bal[self.crrntplyr_counter] += self.bet_val
            
            # for pink button
            if pink_bet:
                if self.plyr_bal[self.crrntplyr_counter] >= self.bet_val:
                    if 'pink' not in self.plyr_choice[self.crrntplyr_counter]:
                        self.plyr_choice[self.crrntplyr_counter].append('pink')
                        self.plyr_bal[self.crrntplyr_counter] -= self.bet_val
                elif 'pink' not in self.plyr_choice[self.crrntplyr_counter]:
                    self.btn_pink.button2reset(self.surface)
            elif not pink_bet and 'pink' in self.plyr_choice[self.crrntplyr_counter]:
                self.plyr_choice[self.crrntplyr_counter].remove('pink')
                if self.plyr_refund:
                    self.plyr_bal[self.crrntplyr_counter] += self.bet_val
            
            # for yellow button
            if yellow_bet:
                if self.plyr_bal[self.crrntplyr_counter] >= self.bet_val:
                    if 'yellow' not in self.plyr_choice[self.crrntplyr_counter]:
                        self.plyr_choice[self.crrntplyr_counter].append('yellow')
                        self.plyr_bal[self.crrntplyr_counter] -= self.bet_val
                elif 'yellow' not in self.plyr_choice[self.crrntplyr_counter]:
                    self.btn_yellow.button2reset(self.surface)
            elif not yellow_bet and 'yellow' in self.plyr_choice[self.crrntplyr_counter]:
                self.plyr_choice[self.crrntplyr_counter].remove('yellow')
                if self.plyr_refund:
                    self.plyr_bal[self.crrntplyr_counter] += self.bet_val
            
            # for violet button
            if violet_bet:
                if self.plyr_bal[self.crrntplyr_counter] >= self.bet_val:
                    if 'violet' not in self.plyr_choice[self.crrntplyr_counter]:
                        self.plyr_choice[self.crrntplyr_counter].append('violet')
                        self.plyr_bal[self.crrntplyr_counter] -= self.bet_val
                elif 'violet' not in self.plyr_choice[self.crrntplyr_counter]:
                    self.btn_violet.button2reset(self.surface)
            elif not violet_bet and 'violet' in self.plyr_choice[self.crrntplyr_counter]:
                self.plyr_choice[self.crrntplyr_counter].remove('violet')
                if self.plyr_refund:
                    self.plyr_bal[self.crrntplyr_counter] += self.bet_val
            
            # bet button
            # if clicked, add 1 to variable self.bet_click then check if player has no bet, if true, decrease player
            # balance value by half of the value of self.bet_val variable then check the value of self.bet_click,
            # if self.bet_click is equal to 1, swap players so that the next player could choose his/her choice of colors
            # if self.bet_click is equal to 2, proceed on animating the lightbulbs  
            if self.btn_bet.button1(self.surface, self.btn_update, self.btn_state):
                self.bet_click += 1
                if self.plyr_choice[self.crrntplyr_counter] == []:
                    self.plyr_bal[self.crrntplyr_counter] -= int(self.bet_val/2)
                
                if self.bet_click == 1:
                    self.btn_state = False
                    self.round_text_update()
                    self.round_text_x_reset()
                    self.round_reset()
                    self.timer_value = self.timer_default_value
                    self.playerswap()
                    self.btn_red.button2reset(self.surface)
                    self.btn_green.button2reset(self.surface)
                    self.btn_blue.button2reset(self.surface)
                    self.btn_pink.button2reset(self.surface)
                    self.btn_yellow.button2reset(self.surface)
                    self.btn_violet.button2reset(self.surface)
                    self.timer_active = False
                
                elif self.bet_click > 1:
                    self.timer_active = False
                    self.timer_value = self.timer_default_value
                    self.colorgame_anim = True
                    self.btn_state = False

            # menu button
            # if clicked, display a window asking if the player really wishes to quit or not
            if self.btn_menu.button1(self.surface, True, self.btn_state_menu):
                self.btn_state = False
                self.btn_state_menu = False
                self.btn_update = False
                self.menu_isActive = True
            
            # fade_animation at start
            if self.fadefrom_active:
                if self.fadefrom.fade(5, self.surface) <= 0:
                    if self.round_delay.delay(1, 10):
                        music.Music.ingame_music1.play(-1)
                        self.fadefrom_active = False
                        self.btn_state_menu = True

            # initial animation
            if self.initial_anim:
                if self.bal_ui1_rect.left < self.bal_ui1_finalleft and self.bal_ui2_rect.right > self.bal_ui2_finalright:
                    self.bal_ui1_rect.left += 3
                    self.bal_ui2_rect.right -= 3
                else:
                    if self.ui_rect.bottom > self.surfacey:
                        self.updatebuttons()
                        self.ui_rect.top -= 4
                    else:
                        self.initial_anim = False
                        self.round_start = True

            # round indicator animation 
            if self.round_start:
                self.round_display()

            # timer 
            if self.timer_active:
                self.timer_def()

            # animate lightbulbs
            if self.colorgame_anim:
                self.animation()

            # activate main game/randomization
            if self.colorgame:
                self.play()

            # reset values
            if self.reset:
                self.plyr_refund = False
                self.reset_values()
            else:
                self.plyr_refund = True
            
            # display end game screen
            if self.winner_isActive:
                self.blitwin()
            
            # displays menu for going back to main menu if true
            if self.menu_isActive:
                menu_state = self.menu_display.display(self.surface)
                # continue the game if resume
                # activate loadscreen quit if quit
                if menu_state == 'resume':
                    self.btn_state = True
                    self.btn_state_menu = True
                    self.btn_update = True
                    self.menu_isActive = False
                elif menu_state == 'quit':
                    music.Music.ingame_music1.stop()
                    self.loadscreen_quit = True

            # display loadscreen before going back to main menu
            if self.loadscreen_quit:
                if self.loading_quit.load(150, self.surface):
                    self.menu_isActive = False
                    self.return_value = 'main_menu'
                    self.loadscreen_quit = False

        # returns the return_value for the state of the game
        return self.return_value
    
    # update button array and initialization
    def updatebuttons(self):
        self.btn_red_array = [self.ui_rect.left + (self.btn_dimen[1]/2) + self.ui_margin, self.ui_rect.centery - (12 * self.scale[1]), [self.btn_red_img, self.btn_red_active_img], self.scale[1], 1, 1]
        self.btn_green_array = [self.btn_red_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_green_img, self.btn_green_active_img], self.scale[1], 1, 1]
        self.btn_blue_array = [self.btn_green_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_blue_img, self.btn_blue_active_img], self.scale[1], 1, 1]
        self.btn_pink_array = [self.btn_blue_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_pink_img, self.btn_pink_active_img], self.scale[1], 1, 1]
        self.btn_yellow_array = [self.btn_pink_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_yellow_img, self.btn_yellow_active_img], self.scale[1], 1, 1]
        self.btn_violet_array = [self.btn_yellow_array[0] + self.btn_space + self.btn_dimen[1], self.ui_rect.centery - (12 * self.scale[1]), [self.btn_violet_img, self.btn_violet_active_img], self.scale[1], 1, 1]
        self.btn_bet_array = [self.ui_rect.right - ((96 * self.scale[1]/2) + self.ui_margin), self.ui_rect.centery - (16 * self.scale[1]), [self.btn_bet_img, self.btn_bet_active_img], self.scale[1], 1.05, 1]
        self.btn_menu_array = [self.ui_rect.left + ((self.btn_menu_img.get_width()/2 * self.scale[1]) + (8 * self.scale[1])), self.ui_rect.top - ((self.btn_menu_img.get_height()/2 * self.scale[1]) + (2 * self.scale[1])), [self.btn_menu_img, self.btn_menu_active_img], self.scale[1], 1, 1]
        self.btn_red = btn.ButtonController(self.btn_red_array)
        self.btn_green = btn.ButtonController(self.btn_green_array)
        self.btn_blue = btn.ButtonController(self.btn_blue_array)
        self.btn_pink = btn.ButtonController(self.btn_pink_array)
        self.btn_yellow = btn.ButtonController(self.btn_yellow_array)
        self.btn_violet = btn.ButtonController(self.btn_violet_array)
        self.btn_bet = btn.ButtonController(self.btn_bet_array)
        self.btn_menu = btn.ButtonController(self.btn_menu_array)

    # function for the round indicator animation at the beginning of every round
    def round_display(self):
        # display all necessary assets(text) for round display
        self.round_surface.set_alpha(self.round_surface_alpha)
        self.surface.blit(self.round_surface, (0, 0))
        self.surface.blit(self.round_shadow_display, (self.round_count_rect.x, self.round_count_rect.y + (5 * (self.scale[1] * 2))))
        self.surface.blit(self.round_count_display, (self.round_count_rect.x, self.round_count_rect.y))
        
        # variables for displaying which player bets/chooses color
        # text render for the player who bets
        plyrturn_render = self.font_round.render("PLAYER " + (str(self.crrntplyr_counter + 1)) + " TURN", False, self.maintxt_clr)
        plyrturn_shadow_render = self.font_round.render("PLAYER " + (str(self.crrntplyr_counter + 1)) + " TURN", False, self.shadow_clr)
        
        # text resize for the player who bets
        plyrturn = pygame.transform.scale(plyrturn_render, (plyrturn_render.get_width() * self.scale[1], plyrturn_render.get_height() * self.scale[1]))
        plyrturn_shadow = pygame.transform.scale(plyrturn_shadow_render, (plyrturn_shadow_render.get_width() * self.scale[1], plyrturn_shadow_render.get_height() * self.scale[1]))
        
        # x and y values of plyrturn
        plyrturn_x = self.round_count_rect.centerx - plyrturn.get_width()/2
        plyrturn_y = self.surfacey/2 

        # display plyrturn
        self.surface.blit(plyrturn_shadow, (plyrturn_x, plyrturn_y + (5 * self.scale[1])))
        self.surface.blit(plyrturn, (plyrturn_x, plyrturn_y))

        # if self.round_state is fadebg, increase alpha value of bg
        # if self.round_state is slidein, slide text through the window
        # if self.round_state is unfadebg, decrease alpha value of bg, 
        # activate timer, and set round_start to False
        if self.round_state == 'fadebg':
            if self.round_surface_alpha <= 200:
                self.round_surface_alpha += 10
            else:
                self.round_state = 'slidein'
        elif self.round_state == 'slidein':
            if self.round_count_rect.x < self.surfacex:
                if self.surfacex > self.surfacey:
                    self.round_count_rect.x += 15 
                else:
                    self.round_count_rect.x += 10
            else:
                self.round_state = 'unfadebg'      
        elif self.round_state == 'unfadebg':
            if self.round_surface_alpha > 0:
                self.round_surface_alpha -= 10
            else:
                self.btn_state = True
                if not self.colorgame_anim and not self.colorgame and not self.reset:
                    self.timer_active = True
                    self.round_surface_alpha = 0
                    self.round_start = False

    # resets the round_start function
    def round_reset(self):
        self.round_start = True
        self.round_state = 'fadebg'

    # updates the text of the round indicator animation
    def round_text_update(self):
        self.round_count_render = self.font_round.render("ROUND " + (str(self.round_count)), False, self.maintxt_clr)
        self.round_shadow_render = self.font_round.render("ROUND " + (str(self.round_count)), False, self.shadow_clr)
        self.round_count_display = pygame.transform.scale(self.round_count_render, (self.round_count_render.get_width() * (self.scale[1] * 2), self.round_count_render.get_height() * (self.scale[1] * 2)))
        self.round_shadow_display = pygame.transform.scale(self.round_shadow_render, (self.round_shadow_render.get_width() * (self.scale[1] * 2), self.round_shadow_render.get_height() * (self.scale[1] * 2)))
        self.round_x = 0 - (self.round_count_display.get_width() + (40 * self.scale[1]))
        self.round_y = self.surfacey/2 - self.round_count_display.get_height()
        self.round_count_rect = self.round_count_display.get_rect()
        self.round_count_rect.topleft = (self.round_x, self.round_y)

    # resets the x position of the round indicator animation for next round
    def round_text_x_reset(self):
        self.round_count_rect.x = self.round_x

    # timer for the game
    def timer_def(self):
        # if self.timer_value is greater than 0, decrease it to one 
        # if not, check if self.plyr_choice is not empty, if it is
        # decrease self.plyr_balance by half of the value of self.bet_val,
        # reset self.timer_value, and check for the value of self.bet_click
        # if self.bet_click is 1, swap players position by calling playerswap()
        # if self.bet_click is 2, set self.colorgame_anim to True
        if self.timer_value > 0:
            if self.timer_delay.delay(1, 60):
                self.timer_value -= 1
                self.timer_delay.reset()
        else:
            self.timer_value = self.timer_default_value
            self.timer_active = False
            if self.plyr_choice[self.crrntplyr_counter] == []:
                self.plyr_bal[self.crrntplyr_counter] -= int(self.bet_val/2)
            self.bet_click += 1
            if self.bet_click == 1:
                self.btn_state = False
                self.btn_red.button2reset(self.surface)
                self.btn_green.button2reset(self.surface)
                self.btn_blue.button2reset(self.surface)
                self.btn_pink.button2reset(self.surface)
                self.btn_yellow.button2reset(self.surface)
                self.btn_violet.button2reset(self.surface)
                self.round_text_update()
                self.round_text_x_reset()
                self.round_reset()
                self.playerswap()
            elif self.bet_click > 1:
                self.colorgame_anim = True
                self.btn_state = False

    # swaps player for next turn
    def playerswap(self):
        self.temp_val = self.crrntplyr_counter
        self.crrntplyr_counter = self.othrplyr_counter
        self.othrplyr_counter = self.temp_val
        self.temp_val = None

    # animation for the lightbulbs before color game
    def animation(self):
        # if statement for repitions of the animation
        # if true, animate the lightbulbs
        # if false, set all the colors to default color, reset counters, set self.colorgame to True, and set self.colorgame_anim to False
        if self.colorgame_anim_ctr1 < 12:
            # if self.colorgame_anim_state is update, change colors depending on value of self.colorgame_anim_ctr2
            # if self.colorgame_anim_state is delay, delay the color change of the animation
            # if self.colorgame_anim_state is reset, add one to both counters and set self.colorgame_anim_state to update
            if self.colorgame_anim_state == 'update':
                # if self.colorgame_anim_ctr2 is less than 4, set color to lightbulbs, if not, set self.colorgame_anim_ctr2 to 0
                if self.colorgame_anim_ctr2 < 4:
                    # if self.colorgame_anim_ctr2 is 0, set all colors to default color
                    # if self.colorgame_anim_ctr2 is 1, set second and third color to default color
                    # if self.colorgame_anim_ctr2 is 2, set first and third color to default color
                    # if self.colorgame_anim_ctr2 is 0, set first and second color to default color
                    if self.colorgame_anim_ctr2 == 0:
                        self.final_result = [0, 0, 0]
                    elif self.colorgame_anim_ctr2 == 1:
                        self.final_result[1], self.final_result[2] = 0, 0
                    elif self.colorgame_anim_ctr2 == 2:
                        self.final_result[0], self.final_result[2] = 0, 0
                    elif self.colorgame_anim_ctr2 == 3:
                        self.final_result[0], self.final_result[1] = 0, 0

                    # If self.colorgame_anim_ctr2 not equal to 0, get a random color 
                    # and store it temporarily to self.final_result.  
                    if self.colorgame_anim_ctr2 != 0:
                        music.Music.randomizer.play()
                        self.final_result[self.colorgame_anim_ctr2 - 1] = random.randint(1, 6)
                    
                    # set self.colorgame_anim_state to delay
                    self.colorgame_anim_state = 'delay'
                else:
                    self.colorgame_anim_ctr2 = 0
            elif self.colorgame_anim_state == 'delay':
                if self.colorgame_delay.delay(1, 12):
                    self.colorgame_delay.reset()
                    self.colorgame_anim_state = 'reset'
            elif self.colorgame_anim_state == 'reset':
                self.colorgame_anim_ctr1 += 1
                self.colorgame_anim_ctr2 += 1
                self.colorgame_anim_state = 'update'
        else:
            self.final_result = [0, 0, 0]
            if self.colorgame_delay.delay(1, 32):
                self.colorgame_delay.reset()
                self.colorgame_anim_ctr1 = 0
                self.colorgame_anim_ctr2 = 0
                self.colorgame = True
                self.colorgame_anim = False

    # function for getting the results and checking if each player has chosen those results
    def play(self):
        # play randomizer done music
        music.Music.randomizer_done1.play()

        # For loop for getting the three random colors for the
        # result and appending those colors to self.temp_result.
        for i in range(3):
            self.result_randomize = random.randint(1, 6)
            self.result_str.append(self.colors[(self.result_randomize)])
            self.temp_result.append(self.result_randomize)
        
        # store values of self.temp_result to self.final_result
        self.final_result = self.temp_result

        # check if colors from self.final_result is in array self.plyr_choice[0]
        for i in self.plyr_choice[0]:
            if i in self.result_str:
                self.plyr_bal[0] += self.bet_val * 2
                self.plyr_displayadd[0] += self.bet_val * 2

        # check if colors from self.final_result is in array self.plyr_choice[1]
        for i in self.plyr_choice[1]:
            if i in self.result_str:
                self.plyr_bal[1] += self.bet_val * 2
                self.plyr_displayadd[1] += self.bet_val * 2

        # set self.displayadd and self.reset to True, and set self.colorgame to False
        self.displayadd = True
        self.reset = True
        self.colorgame = False
    
    # resets the values of all necessary variables
    def reset_values(self):
        if self.reset_delay.delay(1, 50):
            self.btn_red.button2reset(self.surface)
            self.btn_green.button2reset(self.surface)
            self.btn_blue.button2reset(self.surface)
            self.btn_pink.button2reset(self.surface)
            self.btn_yellow.button2reset(self.surface)
            self.btn_violet.button2reset(self.surface)
            self.bet_click = 0
            self.displayadd = False
            self.bet_val *= 2
            self.checkwin()
            if self.winner == None:
                self.plyr_displayadd = [0, 0]
                self.result_str = []
                self.temp_result = []
                self.plyr_choice = [[], []]
                self.reset_delay.reset()
                self.round_count += 1
                self.round_text_update()
                self.round_text_x_reset()
                self.round_reset()
                self.timer_active_delay.reset()
            self.reset = False
    
    # checks if there is a winner
    def checkwin(self):
        # If both self.plyr_bal[0] and self.plyr_bal[1] is less than self.bet_val,
        # check which of the two is greater than the other to determine the winner.
        
        # If not, check if either self.plyr_bal[0] or self.plyr_bal[1] is less than
        # self.bet_val to determine which would be the winner
        if self.plyr_bal[0] < self.bet_val and self.plyr_bal[1] < self.bet_val:
            if self.plyr_bal[0] > self.plyr_bal[1]:
                self.winner = 'PLAYER 1 WON!'
            elif self.plyr_bal[0] < self.plyr_bal[1]:
                self.winner = 'PLAYER 2 WON!'
            elif self.plyr_bal[0] == self.plyr_bal[1]:
                self.winner = 'DRAW'
        else:
            if self.plyr_bal[0] < self.bet_val:
                self.winner = 'PLAYER 2 WON!'
            elif self.plyr_bal[1] < self.bet_val:
                self.winner = 'PLAYER 1 WON!'
        
        # check if self.winner value is not None, if true, call function updatewin()
        # and set self.winner_isActive to True
        if self.winner != None:
            self.updatewin()
            self.winner_isActive = True

    # update the text for whether the player 1 or 2 wins
    def updatewin(self):
        music.Music.ingame_music1.stop()
        if self.winner == 'PLAYER 1 WON!' or self.winner == 'PLAYER 2 WON!':
            music.Music.victory_music.play()
        elif self.winner == 'DRAW':
            music.Music.lose_music.play()
        self.winner_text_render = self.font_round.render(self.winner, False, self.maintxt_clr)
        self.winner_shadow_render = self.font_round.render(self.winner, False, self.shadow_clr)
        if self.winner == 'DRAW':
            scale = self.scale[1] * 2
        else:
            scale = self.scale[1] * 1.25
        self.winner_text = pygame.transform.scale(self.winner_text_render, (self.winner_text_render.get_width() * scale, self.winner_text_render.get_height() * (scale)))
        self.winnder_shadow = pygame.transform.scale(self.winner_shadow_render, (self.winner_shadow_render.get_width() * scale, self.winner_shadow_render.get_height() * (scale)))
        self.winner_text_x, self.winner_text_y = self.surfacex/2 - self.winner_text.get_width()/2, 0 - self.winner_text.get_height()
        self.winner_text_y_center = self.surfacey/3 - self.winner_text.get_height()/2
        self.winner_anim = anim.SlideAnimation(self.winner_text_y)

    # displays the whether the player 1 or 2 wins
    def blitwin(self):
        # display bg
        self.winner_bg.set_alpha(self.winner_bg_alpha)
        self.surface.blit(self.winner_bg, (0, 0))

        # display winner
        if self.winner == 'PLAYER 1 WON!' or self.winner == 'PLAYER 2 WON!':
            self.surface.blit(self.winnder_shadow, (self.winner_text_x, self.winner_text_y + (3 * (self.scale[1] * 2))))
        elif self.winner == 'DRAW':
            self.surface.blit(self.winnder_shadow, (self.winner_text_x, self.winner_text_y + (5 * (self.scale[1] * 2))))
        self.surface.blit(self.winner_text, (self.winner_text_x, self.winner_text_y))

        # if self.winner_state is fadefrom, set self.winner_bg_alpha to a certain value
        # if self.winner_state is displaywin, change self.winner_text_y up until a certain value is met
        # if self.winner_state is displaymes, display text message indicating to click anywhere to continue
        # and if left mouse button is clicked during that time, set self.loadscreen_quit to True
        if self.winner_state == 'fadefrom':
            if self.winner_bg_alpha <= 200:
                self.winner_bg_alpha += 10
            else:
                self.winner_state = 'displaywin'
        elif self.winner_state == 'displaywin':
            if self.winner_text_y < self.winner_text_y_center:
                self.winner_text_y = self.winner_anim.slide('right', 0.5)
            else:
                self.winner_state = 'displaymes'
        elif self.winner_state == 'displaymes':
            if self.winner_displaymes_delay.delay(1, 64):
                self.winner_displaymes.set_alpha(self.winner_displaymes_anim.fadeinout(0, 255, 0.03))
                self.winner_displaymes_shadow.set_alpha(self.winner_displaymes_anim.fadeinout(0, 255, 0.03))
                self.surface.blit(self.winner_displaymes_shadow, (self.surfacex/2 - self.winner_displaymes_shadow.get_width()/2, (self.surfacey/1.5 - self.winner_displaymes_shadow.get_height()/2) + (3 * self.scale[1])))
                self.surface.blit(self.winner_displaymes, (self.surfacex/2 - self.winner_displaymes.get_width()/2, self.surfacey/1.5 - self.winner_displaymes.get_height()/2))
                if pygame.mouse.get_pressed()[0]:
                    if self.winner == 'PLAYER 1 WON!' or self.winner == 'PLAYER 2 WON!':
                        music.Music.victory_music.stop()
                    elif self.winner == 'DRAW':
                        music.Music.lose_music.stop()
                    self.loadscreen_quit = True
    
    # resets all necessary values for the next game
    def hard_reset(self):
        self.crrntplyr_counter = 0
        self.othrplyr_counter = 1
        self.loading.reset()
        self.loading_quit.reset()
        self.fadefrom.reset()
        self.fadefrom_active = True
        self.initial_anim = True
        self.bal_ui1_rect.topleft = (0 - self.bal_ui1.get_width(), 0)
        self.bal_ui2_rect.topright = (self.surfacex + self.bal_ui2.get_width(), 0)
        self.ui_rect.topleft = (self.surfacex/2 - self.ui.get_width()/2, self.surfacey + (120 * self.scale[1]))
        self.updatebuttons()
        self.round_surface_alpha = 0
        self.btn_state_menu = False
        self.btn_update = True
        self.btn_red.button2reset(self.surface)
        self.btn_green.button2reset(self.surface)
        self.btn_blue.button2reset(self.surface)
        self.btn_pink.button2reset(self.surface)
        self.btn_yellow.button2reset(self.surface)
        self.btn_violet.button2reset(self.surface)
        self.bet_click = 0
        self.colorgame_anim = False
        self.colorgame = False
        self.reset = False
        self.colorgame_anim_state = 'update'
        self.colorgame_anim_ctr1 = 0
        self.colorgame_anim_ctr2 = 0
        self.plyr_bal = [1000, 1000]
        self.plyr_displayadd = [0, 0]
        self.plyr_choice = [[], []]
        self.result_str = []
        self.temp_result = []
        self.final_result = [0, 0, 0]
        self.bet_val = 10
        self.round_count = 1
        self.round_start = False
        self.round_state = 'fadebg'
        self.round_text_update()
        self.round_text_x_reset()
        self.timer_active_delay.reset()
        self.reset_delay.reset()
        self.timer_active = False
        self.timer_value = self.timer_default_value
        self.return_value = 'gm2'
        self.winner = None
        self.updatewin()
        self.winner_isActive = False
        self.winner_bg_alpha = 0
        self.winner_state = 'fadefrom'
        self.winner_anim.reset_param()
        self.winner_displaymes_anim.reset()
        self.winner_displaymes_delay.reset()