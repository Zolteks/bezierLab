import pyxel
from lever import Lever
from handle import Handle
from bezier import *
from bezierPlot import Plotter
from aFewQuads import AFewQuads
from spline import Spline

class BezierLab:

    def __init__(self):

        pyxel.init(
            640//1,
            480//1,
            fps=60,
            quit_key=pyxel.KEY_TAB
        )

        self.a = Point(20,220)
        self.b = Point(40,40)
        self.c = Point(310,230)
        self.d = Point(200,40)
        self.bezier = BezierQuad(self.a,self.b,self.c,self.d)
        self.points = 4
        self.plotters = [Plotter(self.bezier)]
        # for quad in Spline().list:
        #     self.plotters.append(Plotter(quad))
        pyxel.run(self.update,self.draw)

    def draw(self):
        pyxel.cls(0)

        for plotter in self.plotters:
            plotter.draw(self.points)

        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, 1, 1, 11)

    def update(self):

        for plotter in self.plotters:
            plotter.update()

        if pyxel.btnp(pyxel.KEY_UP):
            self.a.y -= 1
        if pyxel.btnp(pyxel.KEY_PAGEUP):
            self.points += 1
        if pyxel.btnp(pyxel.KEY_PAGEDOWN):
            if self.points > 1:self.points -= 1

BezierLab()