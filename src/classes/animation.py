import pygame
import math

class HoverAnimation():
    def __init__(self):
        self.x = 0
    
    # hover animation
    def hover(self, y_value:float, hover_height:float, hover_duration:float):
        """
        y_value = y position of the asset when printed on the surface\n
        hover_height = height of which the asset will hover\n
        hover_duration = duration of one hover cycle\n
        """
        newy_value = y_value + hover_height * math.sin(hover_duration * self.x + 0)
        self.x += 1
        return newy_value

    def reset_x(self):
        self.x = 0

class ResizeAnimation():
    def __init__(self, img_values:tuple, ctr_value:int):
        """
        img_values[0] = contains the x position of the image\n
        img_values[1] = contains the y position of the image\n
        img_values[2] = contains the image itself\n
        img_values[3] = contains the scale value of the image\n
        """
        self.img_x, self.img_y = img_values[0], img_values[1]
        self.img = img_values[2]
        self.img_scale = img_values[3]
        self.img_final = pygame.transform.scale(self.img, (self.img_scale * self.img.get_width(), self.img_scale * self.img.get_height()))
        self.img_final_rect = self.img_final.get_rect()
        self.img_final_rect.topleft = (self.img_x - (self.img_final.get_width()/2), self.img_y - (self.img_final.get_height()/2))
        self.x = ctr_value
    
    # resize animation
    def resize(self, scale_size:float, scale_change:float, scale_change_duration:float, surface):
        """
        scale_size = scale of the image\n
        scale_change = scale increase of the image\n
        scale_change_duration = duration of the scale change of the image
        """
        new_value = scale_size + scale_change * math.sin(scale_change_duration * self.x + 0)
        self.x += 1
        self.update(new_value, surface)
    
    # update values 
    def update(self, scale_value:float, surface:tuple):
        self.img_final = pygame.transform.scale(self.img, (scale_value * self.img.get_width(), scale_value * self.img.get_height()))
        self.img_final_rect = self.img_final.get_rect()
        self.img_final_rect.topleft = (self.img_x - (self.img_final.get_width()/2), self.img_y - (self.img_final.get_height()/2))

        surface.blit(self.img_final, (self.img_final_rect.x, self.img_final_rect.y))

    # reset resize
    def reset_x(self):
        self.x = 0

class SlideAnimation():
    def __init__(self, position:int):
       """
       position = can be x or y value
       """
       self.position = position
       self.slide_parameter = 0

    # slide animation
    def slide(self, direction:str, speed:int):
        """
        direction = can only be 'left' or 'right'
        if direction is 'left', position will decrease
        if direction is 'right', position will increase
        """
        if direction == 'left':
            self.position += self.slide_parameter
            self.slide_parameter -= speed
            return self.position
        elif direction == 'right':
            self.position += self.slide_parameter
            self.slide_parameter += speed
            return self.position
    
    # reset slide
    def reset_param(self):
        self.slide_parameter = 0

class FadeFrom():
    def __init__(self, surfacex:int, surfacey:int):
        self.fadefrom_bg = pygame.Surface((surfacex, surfacey))
        self.fadefrom_bg.fill((0, 0, 0))
        self.alpha_val = 255
    
    # fade animation
    def fade(self, speed:int, surface:tuple):
        if self.alpha_val > 0:
            self.alpha_val -= speed
            self.fadefrom_bg.set_alpha(self.alpha_val)
        surface.blit(self.fadefrom_bg, (0, 0))
        return self.alpha_val

    # reset fade
    def reset(self):
        self.alpha_val = 255
        self.fadefrom_bg.set_alpha(self.alpha_val)

class FadeTo():
    def __init__(self, surfacex:int, surfacey:int):
        self.fadeto_bg = pygame.Surface((surfacex, surfacey))
        self.fadeto_bg.fill((0, 0, 0))
        self.alpha_val = 0
    
    # fade animation
    def fade(self, speed:int, surface:tuple):
        if self.alpha_val < 255:
            self.alpha_val += speed
            self.fadeto_bg.set_alpha(self.alpha_val)
        surface.blit(self.fadeto_bg, (0, 0))
        return self.alpha_val

    # reset fade
    def reset(self):
        self.alpha_val = 0
        self.fadeto_bg.set_alpha(self.alpha_val)

class FadeInOut():
    def __init__(self):
        self.param = 0

    def fadeinout(self, alpha_val:float, alpha_change:float, alpha_duration:float):
        
        newalpha_value = alpha_val + alpha_change * math.sin(alpha_duration * self.param + 0)
        self.param += 1
        return newalpha_value

    def reset(self):
        self.param = 0