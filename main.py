import Graphical_Engine.Window as Window
from Graphical_Engine.Font import Font

def main():
    font = Font("assets/fonts/Qlassy.ttf", 30)
    win = Window.Window("Roots of the World")
    
    win.launch()

if __name__ == "__main__":
    main()