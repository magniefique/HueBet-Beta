import pygame
import classes.animation as anim

class Loading():
    def __init__(self, surfacex:int, surfacey:int):
        # surface values
        self.surfacex, self.surfacey = surfacex, surfacey
        
        # bg for loading screen
        self.bg = pygame.Surface((surfacex, surfacey))
        self.bg.fill((0, 0, 0))
        
        self.loading_font = pygame.font.Font("assets/fonts/Sniglet-ExtraBold.ttf", 44)
        self.loading_render = self.loading_font.render('L O A D I N G', False, (255, 255, 255))
        self.loading = pygame.transform.scale(self.loading_render, (self.loading_render.get_width() * (surfacey/640), self.loading_render.get_height() * (surfacey/640)))
        self.loading_anim = anim.FadeInOut()

        # loading screen variable
        self.counter = 0
        
        self.return_value = False
    
    # display loading screen
    def load(self, duration:int, surface:tuple):
        if self.counter < duration:
            surface.blit(self.bg, (0, 0))
            self.loading.set_alpha(self.loading_anim.fadeinout(0, 255, 0.03))
            surface.blit(self.loading, (self.surfacex/2 - self.loading.get_width()/2, self.surfacey/2 - self.loading.get_height()/2))
            self.counter += 1
            self.return_value = False
        else:
            self.return_value = True

        return self.return_value
    
    # resets loading screen
    def reset(self):
        self.counter = 0
        self.loading_anim.reset()