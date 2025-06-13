

class Area:
    def __init__(self, radius=0, length=0, breadth=0):
        self.radius = radius
        self.length = length
        self.breadth = breadth

    def calculate(self):
        pass

class circle(Area):
    def __init__(self, radius):
        super().__init__(radius=radius)

    def calculate(self):
        area = 3.14*(self.radius)**2
        print(f"The area of the circle is: {area}")

class rectangle(Area):
    def __init__(self, length,breadth):
        super().__init__(length=length, breadth=breadth)

    def calculate(self):
        area =  (self.length)*(self.breadth)
        print(f"The area of the rectangle is: {area}")

a = circle(10)
a.calculate()

b = rectangle(5,10)
b.calculate()
