import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, sw_game):
        """Initialize the ship and set its starting position"""
        self.screen = sw_game.screen
        self.screen_rect = sw_game.screen.get_rect()
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Dras the ship at its current location"""
        self.screen.blit(self.image, self.rect)