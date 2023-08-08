# python Object Oriented Programming using class
# the goal is to make calculation of easy area and volume of shapes in mathematics

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter

    def area(self):
        self.area = math.pi * (self.radius**2)
        return self.area

    def sphere_volume(self):
        self.sphere_volume = 4 / 3 * math.pi * (self.radius**3)
        return self.sphere_volume

    def hemisphere_volume(self):
        self.hemisphere_volume = 2 / 3 * math.pi * (self.radius**3)
        return self.hemisphere_volume

class Cylinder(Circle):

    def __init__(self,radius,height):
        super().__init__(radius)
        self.height = height

    def area(self):
        self.area = (2 * math.pi * (self.radius**2)) + (2 * math.pi * self.radius * self.height)
        return self.area

    def volume(self):
        self.volume = math.pi * (self.radius**2) * self.height
        return self.volume

class Cone(Circle):

    def __init__(self,radius,height):
        super().__init__(radius)
        self.height = height

    def slant_height(self):
        self.slant_height = (self.radius**2 + self.height**2) ** 0.5
        return self.slant_height

    def area(self):
        self.area = (math.pi * self.radius**2) + (math.pi * self.radius * self.slant_height)
        return self.area

    def volume(self):
        self.volume = 1/3 * math.pi * (self.radius**2) * self.height
        return self.volume


x = Circle(5)
print(x.radius)
print(x.perimeter())
print(x.area())
print(x.sphere_volume())
print(x.hemisphere_volume())

y = Cylinder(5,20)
print(y.radius)
print(y.height)
print(y.area())
print(y.volume())

z = Cone(5,20)
print(z.slant_height())
print(z.area())
print(z.volume())

