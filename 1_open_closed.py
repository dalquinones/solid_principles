class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Circle):
            return shape.area()
        elif isinstance(shape, Square):
            return shape.area()

shapes = [Circle(5), Square(4)]
calculator = AreaCalculator()
areas = [calculator.calculate_area(shape) for shape in shapes]

'''
PROBLEMA:
AreaCalculator no está cerrado para modificaciones. Si se agrega una nueva forma, 
se debe modificar la clase AreaCalculator, violando el principio OCP.
'''