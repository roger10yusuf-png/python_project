class Shape:
    def __init__(self,name,sides,length):
        self.name = name
        self.sides = sides
        self.length = length
    def perimeter(self):
        result = self.sides * self.length
        print(result)
    def display(self):
        print(self.name, self.sides, self.length)

square1 = Shape("square",4,10)
square1.perimeter()
square1.display()

triangle1 = Shape("triangle",3,7)
triangle1.display()
triangle1.perimeter()
