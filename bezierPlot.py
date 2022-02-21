import pyxel
from handle import Handle
from lever import Lever

class Plotter:

    def __init__(self, quad):
        self.quad = quad
        ah = Handle(quad.p0, 3, 'A')
        bh = Handle(quad.p1, 3, 'B')
        ch = Handle(quad.p2, 3, 'B')
        dh = Handle(quad.p3, 3, 'A')

        self.ab = Lever(ah, bh)
        self.cd = Lever(ch, dh)

    def draw(self, numSegs=4):
        prec = self.quad.p0
        step = 1/numSegs
        for seg in range(1, numSegs+1):
            p0 = self.quad.p(seg * step)
            pyxel.line(p0.x, p0.y, prec.x, prec.y, 13)
            prec = p0

        self.ab.draw()
        self.cd.draw()

    def update(self):
        self.ab.h1.update()
        self.cd.h1.update()
        self.ab.h2.update()
        self.cd.h2.update()
