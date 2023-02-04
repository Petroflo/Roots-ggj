import pygame
from pytmx import load_pygame
import pyscroll

import os

class Map():
    def __init__(self, file_to_load, size):
        self.tmx_data = load_pygame(file_to_load)
        print("self.tmx_data: " + str(self.tmx_data))
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, size)
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=5)
        self.map_layer.zoom = 2
    
    def reload(self, file_to_load):
        self.tmx_data = load_pygame(file_to_load)
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.map_layer.size)
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=5)
        self.map_layer.zoom = 2
    
    
    def center(self, point):
        self.map_layer.center(point)
    
    def return_object(self, name):
        return self.tmx_data.get_object_by_name(name)
    
    def add_sprite(self, sprite):
        self.group.add(sprite)

    def draw(self, screen):
        self.group.draw(screen)
    
    def update(self, screen):
        self.group.update(screen)
    
    def get_group(self):
        return self.group