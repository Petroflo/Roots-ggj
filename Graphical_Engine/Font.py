import pygame
from Graphical_Engine.Colors import get_colors

class Font():
    def __init__(self, file, size=32):
        pygame.font.init()
        self.default_color = "black"
        self.default_bg_color = "white"
        self.default_size = size
        self.file_path = file
        self._font = pygame.font.Font(file, self.default_size)
        print("Font loaded: " + file)

    def getFont(self):
        return self._font

    def rescale(self, scale):
        self._font = pygame.font.Font(self.file_path, int(self.default_size * scale[0]))
