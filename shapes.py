class Shape:
    def __init__(self,name,sides,length,width):
        self.name = name
        self.sides = sides
        self.length = length
        self.width = width
    def perimeter(self):
        result = self.sides * self.length
        print(result)
    def area(self):
        result = self.length * self.width
        print(result)
    def display(self):
        print(self.name, self.sides, self.length)

square1 = Shape("square",4,10,10)
square1.perimeter()
square1.display()
square1.area()

triangle1 = Shape("triangle",3,7,5)
triangle1.display()
triangle1.perimeter()
triangle1.area()

rectangle1 = Shape("rectangle",4,7,14)
rectangle1.display()
rectangle1.perimeter()
rectangle1.area()

