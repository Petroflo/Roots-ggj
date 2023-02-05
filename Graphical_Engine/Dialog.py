import random
import pygame
import os

class DialogBox:

    x = 60
    y = 450

    def __init__(self):
        self.box = pygame.image.load(os.path.join("assets", "dialogs", "dialog_box.png"))
        self.texts = ["Hello World!", "Il y a longtemps, les hommes se sont réunis pour savoir quelque chose sur qu'elqu'un de trés misterieux. Un homme Balur s'est proposé pour les guider, d'autres voulaient la guerre, d'autres voulaient des lois.", "Quel choix aurions-nous dû faire ?"]
        self.text_index = 0
        self.letter_index = 0
        #self.font = pygame.font.Font("assets/fonts/Qlassy.ttf", 20)
        self.font = pygame.font.SysFont("TimesNewRoman", 28)
        self.reading = False

    def start_dialog(self):
        if self.reading:
            self.next_speech()
        else:
            self.reading = True
            self.text_index = 0

    def render(self, screen):
        clock = pygame.time.Clock()
        self.box = pygame.transform.scale(self.box, (screen.get_height() * .8, screen.get_width() * .4))
        if self.reading:
            self.letter_index += 1
                
            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index
            screen.blit(self.box, (self.x, self.y))

            # text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
            # screen.blit(text, (self.x + 60, self.y + 30))
            text = self.texts[self.text_index]
            pos = self.x + 60, self.y + 30
            words = [word.split(' ') for word in text.split()]  # 2D array where each row is a list of words.
            space = self.font.size(' ')[0]  # The width of a space.
            max_width, max_height = self.box.get_size()
            x, y = pos
            for line in words:
                for word in line:
                    word_surface = self.font.render(word[0:self.letter_index], False, (0, 0, 0))
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= max_width:
                        x = pos[0]  # Reset the x.
                        y += word_height  # Start on new row.
                    screen.blit(word_surface, (x, y))
                    x += word_width + space

    def next_speech(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False