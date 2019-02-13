from Shape import Shape


class Rectangle(Shape):
    def __str__(self, xcor, ycor, width, height):
        Shape.__init__(self, xcor, ycor)
        self.width = width
        self.height = height
