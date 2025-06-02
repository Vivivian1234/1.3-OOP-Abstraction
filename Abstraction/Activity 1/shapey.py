from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3


class Rectangle(Shape):
    def __init__(self, width, height, depth=1):
        self.width = width
        self.height = height
        self.depth = depth

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def volume(self):
        # Volume of a rectangular prism
        return self.width * self.height * self.depth


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def volume(self):
        # Volume of a cube
        return self.side ** 3
