import pyxel

class Lever:

    def __init__(self, h1, h2):
        self.h1 = h1
        self.h2 = h2

    def draw(self):
        pyxel.line(self.h1.p.x, self.h1.p.y, self.h2.p.x, self.h2.p.y, 8)
        self.h1.draw()
        self.h2.draw()