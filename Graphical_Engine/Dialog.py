import random
import pygame
import os

class DialogBox:

    x = 60
    y = 450

    def __init__(self):
        self.box = pygame.image.load(os.path.join("assets", "dialogs", "dialog_box.png"))
        self.box = pygame.transform.scale(self.box, (700, 130))
        self.texts = ["Hello World!", "Coucou", "Poulet", "Pieds"]
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