import pygame, sys, os

pygame.init()

Colors = [
    {"name": "black", "value": (0, 0, 0)},
    {"name": "white", "value": (255, 255, 255)},
    {"name": "red", "value": (255, 0, 0)},
]

class Window:
    def __init__(self, width, height, title):
        self.size = (width, height)
        self.title = title,
        self.running = True
        self.screen = pygame.display
        self.screen.set_mode(self.size, pygame.RESIZABLE)
        self.screen.set_caption("My Game", "")
    
    def launch(self):
        print("Launching window...")
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If the user clicks the close button
                    self.running = False
                    pygame.quit()
                    sys.exit()
                pygame.mouse.set_visible(True)
                if pygame.mouse.get_pressed()[0]:
                    print("Clicked")
                    print(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        pygame.quit()
                        sys.exit()

            self.screen.update()
            
