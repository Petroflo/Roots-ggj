import pygame, sys, os, Graphical_Engine.Colors as Colors, pyscroll, pytmx
from pytmx import load_pygame
import Graphical_Engine.Elements.Element as Element


pygame.init()

class Window:
    def __init__(self, width, height, title):
        self.size = (width, height)
        self.width = width
        self.height = height
        self.title = title,
        self.scale = (1, 1)
        self.running = True
        self.screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self.elements = []
    
        tmx_data = pytmx.util_pygame.load_pygame(f"./assets/maps/world.tmx")

        self.map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = 2
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=2)
        #selfgroup.add(self.player)

    def add_element(self, element):
        self.elements.append(element)
        
    def remove_element(self, element):
        self.elements.remove(element)

    def launch(self):
        print("Launching window...")
        while self.running:
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if (event.type == pygame.QUIT): # If the user clicks the close button or presses escape
                    self.running = False
                    pygame.quit()
                    sys.exit()
                pygame.mouse.set_visible(True)
                if pygame.mouse.get_pressed()[0]:
                    print("Clicked")
                    print(pygame.mouse.get_pos())
                # event related to resizing the window
                if event.type == pygame.VIDEORESIZE:
                    print("Resizing window...")
                    # print new window size
                    print(event.w, event.h)
                    self.scale = (event.w / self.width, event.h / self.height)
                    self.size = (event.w, event.h)
                    self.width = event.w
                    self.height = event.h
                    for el in self.elements:
                        el.rescale(self.scale)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        sys.exit()
            # for el in self.elements:
            #     if (el.active):
            #         el.draw()
            pygame.display.flip()