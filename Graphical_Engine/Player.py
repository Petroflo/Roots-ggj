import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, file_to_load, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load(file_to_load)
        print("self.sprite_sheet: " + str(self.sprite_sheet))
        self.position = [x, y]
        self.speed = 1
        self.running = False
        self.moving = [0, 0]

        self.looks = {
            "down": 0,
            "left": 1,
            "right": 2,
            "up": 3
        }
        
        self.walk = 1
        self.current_look = "down"

        self.image = self.get_image(self.walk, self.looks["down"])
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
    
    def stay(self):
        self.walk = 1
        self.image = self.get_image(self.walk, self.looks[self.current_look])
        self.image.set_colorkey((0, 0, 0))
        return self.image

    def walk_animation(self):
        self.walk += 1
        if (self.walk > 2):
            self.walk = 0
        print(self.current_look)
        self.image = self.get_image(self.walk, self.looks[self.current_look])
        self.image.set_colorkey((0, 0, 0))


    def key_pressed(self, key):
        if key[pygame.K_UP]:
            self.moving[1] = - 5
            self.current_look = "up"
        if key[pygame.K_DOWN]:
            self.moving[1] = 5
            self.current_look = "down"
        if key[pygame.K_LEFT]:
            self.moving[0] = -5
            self.current_look = "left"
        if key[pygame.K_RIGHT]:
            self.moving[0] = 5
            self.current_look = "right"
            
    def key_released(self, event):
        if (event.key == pygame.K_UP):
            if (self.moving[0] == -5):
                self.current_look = "left"
            elif (self.moving[0] == 5):
                self.current_look = "right"
            self.moving[1] = 0
        elif (event.key == pygame.K_DOWN):
            if (self.moving[0] == -5):
                self.current_look = "left"
            elif (self.moving[0] == 5):
                self.current_look = "right"
            self.moving[1] = 0
        elif (event.key == pygame.K_LEFT):
            if (self.moving[1] == -5):
                self.current_look = "up"
            elif (self.moving[1] == 5):
                self.current_look = "down"
            self.moving[0] = 0
        elif (event.key == pygame.K_RIGHT):
            if (self.moving[1] == -5):
                self.current_look = "up"
            elif (self.moving[1] == 5):
                self.current_look = "down"
            self.moving[0] = 0

    # moving = [x, y]
    def move(self):
        self.position[0] += (self.moving[0] * self.speed)
        self.position[1] += (self.moving[1] * self.speed)
        if (self.moving[0] != 0 or self.moving[1] != 0):
            self.walk_animation()
        else:
            self.stay()
         
    def update(self, screen):
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        screen.blit(self.image, self.rect)
        
    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x * 32, y * 32, 32, 32))
        return image
    
    