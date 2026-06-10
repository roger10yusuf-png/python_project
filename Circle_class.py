class Circle():
    def __init__(self,radius,color,x_pos,y_pos):
        self.radius = radius
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos

    def area(self):
            result_a = 2 * 3.14 * (self.radius ** 2)
            print(result_a)
    def display(self):
            print(self.radius,self.color,self.x_pos,self.y_pos)

circle1 = Circle(55,"green",25,57)
circle1.area()
circle1.display()
