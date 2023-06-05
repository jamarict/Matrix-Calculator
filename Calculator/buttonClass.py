from cmu_graphics import *

class Button:
    def __init__(self, x, y, size, text, fun, color):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.function = fun
        self.color = color
        self.border = "black"
        self.canEdit = False
        self.canDisplay = False

    def draw(self):
        drawLabel(self.text, self.x, self.y, size = self.size, font = "monospace")

class CircleButton(Button):
    def __init__(self,x,y,r, size, text,fun,color):
        super().__init__(x,y, size, text,fun,color)
        self.r = r

    def draw(self):
        drawCircle(self.x, self.y, self.r, fill = self.color)
        super().draw()

    def checkForPress(self, app, mX, mY):
        if ((mX - self.x) ** 2 + (mY-self.y) **2) ** 0.5 <= self.r:
            self.function(app)

class RectangleButton(Button):
    def __init__(self,x,y,w,h,size, text,fun,color):
        super().__init__(x,y,size, text,fun,color)
        self.width = w
        self.height = h

    def draw(self):
        x = self.x - self.width/2
        y = self.y - self.height/2
        drawRect(x,y,self.width,self.height, fill= self.color, borderWidth = 5, border = self.border)
        super().draw()

    def checkForPress(self,app,mX,mY):
        if (self.x - self.width/2 <= mX <= (self.x + self.width/2)) and (self.y - self.height/2 <= mY <= (self.y + self.height/2)):
            self.function(app)
        
