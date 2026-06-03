class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        print(result)
    def perimeter(self):
        result = 2 * (self.length + self.width)
        print(result)
    def display(self):
        print(self.length,self.width)

rectangle1 = Rectangle(7,14)
rectangle1.area()
rectangle1.perimeter()
rectangle1.display()

