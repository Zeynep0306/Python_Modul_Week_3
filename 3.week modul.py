class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)


rect1 = Rectangle(5, 7)
print("dikdortgenin alani: ", rect1.area())
print("dikdrtgenin cevresi:", rect1.perimeter())