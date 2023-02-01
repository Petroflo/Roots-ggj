import pygame
import Graphical_Engine.Colors as Colors
import Graphical_Engine.Elements.Element as Element

class Speech_Box (Element.Element):
    def __init__(self, text, bg_color, x, y, width, height, screen, fixed):
        super().__init__()
        self.text = text
        self.bg_color = Colors.get_colors(bg_color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.name = "Speech Box :" + text
        self.fixed = fixed
    
    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, (self.x, self.y, self.width, self.height))
        
    def rescale(self, scale):
        if (self.fixed == True):
            return
        self.x *= scale[0]
        self.y *= scale[1]
        self.width *= scale[0]
        self.height *= scale[1]
