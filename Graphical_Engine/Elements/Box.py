import Graphical_Engine.Elements.Element as Element
import Graphical_Engine.Colors as Colors
import pygame

class Box (Element.Element):
    def __init__(self, x, y, width, height, screen, color="white", fixed=False):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.bg_color = Colors.get_colors(color)
        self.fixed = fixed
    
    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, (self.x, self.y, self.width, self.height))  
    
    def rescale(self, scale):
        print("Rescaling Box")
        print("scale: " + str(scale))
        if (self.fixed == True):
            return
        self.x *= scale[0]
        self.y *= scale[1]
        self.width *= scale[0]
        self.height *= scale[1]