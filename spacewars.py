import sys
import pygame
from settings import Settings
from ship import Ship

class SpaceWars:
    """Overall class to manage game assets and behaviour"""
    
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Wars")
        self.ship = Ship(self)
        
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()  
            self.clock.tick(60)
            
if __name__ == '__main__':
    sw = SpaceWars() 
    sw.run_game()
