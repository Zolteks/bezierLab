class Point:

    def __init__(self, x, y):
        self.x = x/1.0
        self.y = y/1.0
        # self.y = 240-y/1.1

    def __str__(self):
        return f"{self.x},{self.y}"

class BezierQuad:

    def __init__(self, p0, p1, p2, p3):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def  p(self, p):

        self.u1 = self.interpolate(self.p0, self.p1, p)
        self.u2 = self.interpolate(self.p1, self.p2, p)
        self.u3 = self.interpolate(self.p2, self.p3, p)

        self.v1 = self.interpolate(self.u1, self.u2, p)
        self.v2 = self.interpolate(self.u2, self.u3, p)

        return self.interpolate(self.v1, self.v2, p)
    
    def interpolate(self, p1, p2, perc):
        vx = (p2.x-p1.x) * perc
        vy = (p2.y-p1.y) * perc
        return Point(vx + p1.x, vy + p1.y)