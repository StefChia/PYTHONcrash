import pygame
from random import randint
from pygame.sprite import Sprite

class Spell(Sprite):
    """Define a spell that gives the ship super powers"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.spell_color
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.spell_width,
            self.settings.spell_height)
        self.rect.y = 0
        self.rect.x = randint(0,self.settings.screen_width-self.settings.spell_width)

        # Store the position as a float.
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the spell down the screen."""
        # Update the exact position of the bullet.
        self.y += self.settings.spell_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_spell(self):
        """Draw the spell to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)