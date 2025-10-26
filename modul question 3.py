class Shape:
    def __init__(self,width,height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__ (self, side):
        super().__init__(side, side)
    def calculate_area(self):
        return self.width * self.height

rectangle= Rectangle(10,3)
print("rectangle area:" , rectangle.calculate_area())

square= Square(5)
print("square area : ", square.calculate_area())