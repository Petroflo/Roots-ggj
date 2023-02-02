import Graphical_Engine.Window as Window
from Graphical_Engine.Elements.Box import Box
from Graphical_Engine.Elements.Speech_Box import Speech_Box
from Graphical_Engine.Font import Font
from screeninfo import get_monitors

size = (0, 0)

for m in get_monitors():
    size = (m.width, m.height)


win = Window.Window(int(size[0] * .9), int(size[1] * .9), "My Game")
font = Font("assets/fonts/Qlassy.ttf", 30)
box = Box(0, 0, size[0], size[1], win.screen, "white", True)
speech = Speech_Box(box, font, "Salut, comment vas tu ?")

win.add_element(box)
win.add_element(speech)

print(win.elements)
win.launch()