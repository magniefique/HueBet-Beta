import pygame

pygame.init()

class Music():
    # bg music
    main_menu_music = pygame.mixer.Sound('assets/music/menu.mp3')
    ingame_music1 = pygame.mixer.Sound('assets/music/ingame.mp3')
    
    # mouse click
    mouse_sound = pygame.mixer.Sound('assets/music/click.mp3')

    # randomizer sound
    randomizer = pygame.mixer.Sound('assets/music/randomizer.wav')
    randomizer_done1 = pygame.mixer.Sound('assets/music/randomizer_done1.wav')
    randomizer_done2 = pygame.mixer.Sound('assets/music/randomizer_done2.wav')

    # victory and lose music
    victory_music = pygame.mixer.Sound('assets/music/victorymusic.mp3')
    lose_music = pygame.mixer.Sound('assets/music/losemusic.mp3')