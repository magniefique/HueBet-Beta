import pygame
import math
import classes.animation as anim

class ButtonController():

    def __init__(self, button_values:tuple):
        """
        button_values[0] contains the x location of the top left of the button\n
        button_values[1] contains the y location of the top left of the button\n
        button_values[2] contains the image file/s used for the button\n
        button_values[3] contains the scale/scale of the button\n
        button_values[4] contains the size/scale of the button when hovered\n
        button_values[5] contains the type of button (Static or Hovering)\n
        """
        self.buttonx, self.buttony = button_values[0], button_values[1]
        self.button_image = button_values[2]
        default_image_counter = 0
        self.width = self.button_image[default_image_counter].get_width()
        self.height = self.button_image[default_image_counter].get_height()
        self.default_scale = button_values[3]
        self.hover_scale = self.default_scale * button_values[4]
        self.button_type = button_values[5]
        self.image = pygame.transform.scale(self.button_image[default_image_counter], (int(self.width * button_values[3]), int(self.height * button_values[3])))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.buttonx - int(self.width * self.default_scale/2), self.buttony - int(self.height * self.default_scale/2))
        self.action = False
        self.isClicked = False
        self.isPressed = False
        self.animation_self = anim.HoverAnimation()
        self.x = 0

    # function that updates the button image, location, and scale
    def update(self, image_counter:int, scale_value:float, isAnimating:bool):
        self.image = pygame.transform.scale(self.button_image[image_counter], (int(self.width * scale_value), int(self.height * scale_value)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.buttonx - int(self.width * scale_value/2), self.buttony - int(self.height * scale_value/2))
        # checks if the button is animating or not     
        if isAnimating:
            self.rect.y =  self.animation_self.hover((self.buttony - self.image.get_height()/2), 4, 0.05)
        else:
            self.rect.topleft = (self.buttonx - int(self.width * scale_value/2), self.buttony - int(self.height * scale_value/2))
            self.animation_self.reset_x()

    # function for a button
    def button1(self, surface, isUpdate, isActive):
        """
        Function for an on-click button.
        """
        action = False
        if isUpdate:
            mouse_pos = pygame.mouse.get_pos()
                
            if self.rect.collidepoint(mouse_pos):
                scale_value, animationstate = self.hover(True, self.isPressed, self.button_type)[0], self.hover(True, self.isPressed, self.button_type)[1]
                if pygame.mouse.get_pressed()[0] == 1 and self.isPressed == False and self.isClicked == False and isActive:
                    self.isClicked = True
                    self.isPressed = self.click(True, self.isPressed, scale_value, animationstate)
                    action = True
                elif pygame.mouse.get_pressed()[0] == 1 and self.isPressed == True and self.isClicked == False and isActive:
                    self.isClicked = True
                    self.isPressed = self.click(True, self.isPressed, scale_value, animationstate)
                    action = False
            else:
                self.hover(False, self.isPressed, 1)

            if pygame.mouse.get_pressed()[0] == 0:
                self.isClicked = False
                self.isPressed = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

    # function for a lever-type button
    def button2(self, surface, isUpdate, isActive):
        """
        Function for a lever-type button.
        """
        if isUpdate:
            mouse_pos = pygame.mouse.get_pos()
                
            if self.rect.collidepoint(mouse_pos):
                scale_value, animationstate = self.hover(True, self.isPressed, self.button_type)[0], self.hover(True, self.isPressed, self.button_type)[1]
                if pygame.mouse.get_pressed()[0] == 1 and self.isPressed == False and self.isClicked == False and isActive:
                    self.isClicked = True
                    self.isPressed = self.click(True, self.isPressed, scale_value, animationstate)
                    self.action = True
                elif pygame.mouse.get_pressed()[0] == 1 and self.isPressed == True and self.isClicked == False and isActive:
                    self.isClicked = True
                    self.isPressed = self.click(True, self.isPressed, scale_value, animationstate)
                    self.action = False
            else:
                self.hover(False, self.isPressed, 1)

            if pygame.mouse.get_pressed()[0] == 0:
                self.isClicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return self.action

    def button2reset(self, surface):
        if self.isPressed:
            self.isPressed = self.click(True, self.isPressed, self.default_scale, False)
            self.action = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return self.action

    # function for click event
    def click(self, clicked:bool, activated:bool, scale_value:float, animation:bool):      
        if clicked and not activated:
            button_img_ctr = 1
            return_value = True
        elif clicked and activated:
            button_img_ctr = 0
            return_value = False
        elif not clicked and activated:
            button_img_ctr = 1
            return_value = activated
        elif not clicked and not activated:
            button_img_ctr = 0
            return_value = activated

        self.update(button_img_ctr, scale_value, animation)
        return return_value

    # function for hover event 
    def hover(self, isHover:bool, activated:bool, buttontype:int):
        if activated:
            button_image_ctr = 1
            if isHover:
                scale_value = self.hover_scale
            else:
                scale_value = self.default_scale
        else:
            button_image_ctr = 0   
            if isHover:
                scale_value = self.hover_scale
            else:
                scale_value = self.default_scale

        if buttontype == 1:
            animation = False
        elif buttontype == 2 and isHover:
            animation = True
        elif buttontype == 2 and not isHover:
            animation = False
        
        self.update(button_image_ctr, scale_value, animation)
        return scale_value, animation