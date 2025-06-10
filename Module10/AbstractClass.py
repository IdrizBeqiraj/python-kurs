from abc import ABC

class ClassName(ABC): #this is the final definition of an abstract class ABC is important
    pass

class Shape(ABC): #klase abstrakte
    #metode abstrakte
    @abstraktmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius


from abc import ABC, abstractmethod


class Shape(ABC):  # Klasa abstrakte
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):         # Krijimi i klasës për katrorin
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


circle = Circle(5)
square = Square(4)

print("Circle area:", circle.area())
print("Square area:", square.area())

#klasat abstrakte mund te kene edhe metoda te thjeshta dhe abstrakte
#interface jane klasa abstrakte qe kane vetem metoda abstrakte
