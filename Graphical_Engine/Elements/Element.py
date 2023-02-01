class Element:
    def __init__(self):
        self.active = True
        print("Element created")

    def switch_active(self):
        self.active = not self.active

    def draw(self):
        print("Element drawn")
        
    def rescale(self, scale):
        print("Element rescaled")