import pygame
import Graphical_Engine.Colors as Colors
import Graphical_Engine.Elements.Element as Element
import Graphical_Engine.Elements.Box as Box

class Speech_Box (Element.Element):
    def __init__(self, Box, font, text, bg_color="white", color="black", fixed=False):
        super().__init__()
        self.fixed = fixed
        self.bg_color = Colors.get_colors(bg_color)
        self.color = Colors.get_colors(color)
        self.font = font
        self.box = Box
        self.font_object = font.getFont()
        self.text = self.font_object.render(text, True, self.color, self.bg_color)

    def draw(self):
        rect = self.text.get_rect()
        rect.move_ip((self.box.width - rect.width) / 2, (self.box.height - rect.height) / 2)
        self.box.screen.blit(self.text, rect)
        
    def rescale(self, scale):
        if (self.fixed == True):
            return
        self.font.rescale(scale)

