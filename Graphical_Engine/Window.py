import pygame
import sys
import os 
import Graphical_Engine.Colors as Colors

from pytmx import load_pygame
import pyscroll
from Graphical_Engine.Dialog import DialogBox

from Graphical_Engine.Map import Map
from Graphical_Engine.Player import Player

pygame.init()

class Window:
    def __init__(self, title):
        self.running = True
        self.width = 600
        self.height = 800
        self.title = title
        self.screen = pygame.display.set_mode((800, 600))
        self.Map = Map(os.path.join("assets", "maps", "basic_map", "world.tmx"), (800, 600))
        self.dialog_box = DialogBox()
        self.key = None
        self.player = None
        self.create_player()

    def create_player(self):
        player_position = self.Map.return_object("player_1")
        self.player = Player(os.path.join("assets", "sprites", "player.png"), player_position.x, player_position.y)
        self.Map.add_sprite(self.player)

    def execute_key_event(self):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_BACKSPACE]:
            print("Backspace pressed")
            self.dialog_box.start_dialog()
        self.player.key_pressed(self.key)
        # key liés au jeu (m pour afficher l'arbre des décisions prises)
        
    def get_event(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                print("Closing window...")
                self.running = False
                print(self.running)
            elif event.type == pygame.KEYDOWN:
                self.execute_key_event()
            elif event.type == pygame.KEYUP:
                self.player.key_released(event)

    def launch(self):
        clock = pygame.time.Clock()
        pygame.key.set_repeat()
        while self.running:
            self.get_event()
            self.player.move(self.Map.get_walls())
            self.Map.center(self.player.rect.center)
            self.Map.update(self.screen)
            self.Map.draw(self.screen)
            self.dialog_box.render(self.screen)
            clock.tick(60)
            pygame.display.flip()
        pygame.quit()
        sys.exit()
        