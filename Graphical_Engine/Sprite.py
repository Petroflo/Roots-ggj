import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, file_to_load, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load(file_to_load)
        print("self.sprite_sheet: " + str(self.sprite_sheet))
        # get second image on the first row
        self.image = self.get_image(1, 0)
        self.image.set_colorkey((0, 0, 0))
        print("self.image: " + str(self.image))
        self.rect = self.image.get_rect()
        self.position = [x, y]
    
    # moving = [x, y]
    def move(self, moving):
        self.position[0] += moving[0]
        self.position[1] += moving[1]
         
    def update(self, screen):
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        screen.blit(self.image, self.rect)
        
    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x * 32, y * 32, 32, 32))
        return image
    
    