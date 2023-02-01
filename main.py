import Graphical_Engine.Window as Window

size = (0, 0)

from screeninfo import get_monitors
for m in get_monitors():
    size = (m.width, m.height)

screen = Window.Window(int(size[0]), int(size[1]), "My Game")
screen.launch()    

# screen = Window.Window(800, 600, "My Game")
# print(screen)

# screen.launch()