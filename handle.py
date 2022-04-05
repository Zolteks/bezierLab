import pyxel

class Handle:

    def __init__(self, p, s, t):
        self.p = p
        self.size = s
        self.center = self.size/2
        self.updateGPos()
        self.type = t
        self.holding = False
        self.press = False

    def draw(self):
        if self.type == 'A':
            pyxel.rect(self.gx, self.gy, self.size, self.size, 10)
        else:
            pyxel.circ(self.p.x, self.p.y, self.size/2, 5)
        pyxel.rect(self.p.x,self.p.y, 1, 1, 7)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.hit(pyxel.mouse_x, pyxel.mouse_y):
                self.offsetX = pyxel.mouse_x - self.p.x
                self.offsetY = pyxel.mouse_y - self.p.y
                self.holding = True
                print(id(self))

        if self.holding:
            self.updatePos()
            self.updateGPos()
            if not pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.holding = False
    
    def updateGPos(self):
        self.gx = self.p.x - self.center
        self.gy = self.p.y - self.center
    
    def hit(self, x, y):
        return x >= self.gx and x < self.gx + self.size and y >= self.gy and y < self.gy + self.size

    def updatePos(self):
        self.p.x = pyxel.mouse_x - self.offsetX
        self.p.y = pyxel.mouse_y - self.offsetY
