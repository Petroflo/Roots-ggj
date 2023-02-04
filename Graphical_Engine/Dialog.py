import random
import pygame
import os

class DialogBox:

    x = 60
    y = 450

    def __init__(self):
        self.box = pygame.image.load(os.path.join("assets", "dialogs", "dialog_box.png"))
        self.box = pygame.transform.scale(self.box, (700, 130))
        self.texts = ["Hello World!", "Coucou", "Poulet", "Pieds", "Il y a longtemps, les hommes se sont réunis pour savoir vers qui se tourner. Un homme Balur s'est proposé pour les guider, d'autres voulaient la guerre, d'autres voulaient des lois. Quel choix aurions-nous dû faire ?"]
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("assets/fonts/dialog_font.ttf", 20)
        #self.font = pygame.font.SysFont("TimesNewRoman", 20)
        self.reading = False

    def start_dialog(self):
        if self.reading:
            self.next_speech()
        else:
            self.reading = True
            self.text_index = 0

    def blit_text(surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def render(self, screen):
        if self.reading:
            self.letter_index += 1

            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index

            screen.blit(self.box, (self.x, self.y))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
            screen.blit(text, (self.x + 60, self.y + 30))

    def next_speech(self):
        #self.text_index = self.texts[random.randint(0, len(self.texts) - 1)]
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False