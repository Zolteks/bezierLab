from bezier import *

class Spline:
    
    def __init__(self):
        self.list = []
        a = Point(277.2, 94.0, "a")
        b = Point(281.2, 69.6, "b")
        c = Point(271.5, 54.0, "c")
        d = Point(254.9, 52.2, "d")
        print(id(d))
        self.list.append(BezierQuad(a, b, c, d))
        a = d
        b = Point(231.7, 49.7, "b")
        c = Point(212.9, 71.0, "c")
        d = Point(209.4, 93.4, "d")
        print(id(a))
        self.list.append(BezierQuad(a, b, c, d))
        a = d
        b = Point(205.4, 118.9, "b")
        c = Point(218.4, 130.2, "c")
        d = Point(231.5, 132.3, "d")
        self.list.append(BezierQuad(a, b, c, d))

    def quad(self, pId):
        for quad in self.list:
            if id(quad.p1) == pId or id(quad.p2) == pId:
                return quad, 