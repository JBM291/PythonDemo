class Shape:
    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor

    def __str__(self):
        return 'x": ' +str(self.x) + ' y: ' + str(self.y)

    def move(self,x1, y1):
        self.x = self.x + x1
        self.y = self.y + y1

