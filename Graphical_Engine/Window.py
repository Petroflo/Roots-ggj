import pygame
import sys
import os 
import Graphical_Engine.Colors as Colors

from pytmx import load_pygame
import pyscroll

from Graphical_Engine.Map import Map
from Graphical_Engine.Player import Player

pygame.init()

class Window:
    def __init__(self, title):
        self.running = True
        self.width = 600
        self.height = 800
        self.title = title,
        self.screen = pygame.display.set_mode((800, 600))
        file_to_load = os.path.join("assets", "maps", "basic_map", "world.tmx")
        self.Map = Map(file_to_load, (800, 600))
        player_position = self.Map.return_object("player_1")
        self.player = Player(os.path.join("assets", "sprites", "player.png"), player_position.x, player_position.y)
    
        self.Map.add_sprite(self.player)
        self.key = None

    def execute_key_event(self):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_ESCAPE]:
            print("Closing window...")
            pygame.quit() 
            self.running = False
            sys.exit()
        self.player.key_pressed(self.key)
        
    def get_event(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                print("Closing window...")
                pygame.quit()
                self.running = False
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                print("Resizing window...")
                self.size = (event.w, event.h)
                self.width = event.w
                self.height = event.h
            elif event.type == pygame.KEYDOWN:
                self.execute_key_event()
            elif event.type == pygame.KEYUP:
                self.player.key_released(event)

    def launch(self):
        clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 1)
        while self.running:
            self.get_event()
            self.player.move()
            self.Map.center(self.player.rect.center)
            self.Map.update(self.screen)
            self.Map.draw(self.screen)
            clock.tick(60)
            pygame.display.flip()
        