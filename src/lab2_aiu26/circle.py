import math
from lab2_aiu26.shape import Shape, type_error, number_error



class Circle(Shape): #class for creating circles
    def __init__(self, radius: float, x: float = 0, y: float = 0):
          super().__init__(x,y)
          type_error(radius, "radius")
          number_error(radius, "radius")
          self.radius = radius
    @property # read only property for calculating area
    def area(self) -> float:
        return math.pi * self.radius ** 2

    @property # read only property for calculating perimeter
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def is_circle_unit(self) -> bool: # function to check if circle is unit
         return self.radius == 1

    def __str__(self): #function to display the circle object
         return f"Circle has radius = {self.radius} and position: x = {self.x}, y = {self.y}"
    def __repr__(self): #function to display the circle object i a more detailed way
         return f"Circle:(radius:{self.radius}, x:{self.x}, y:{self.y})"


    def __eq__(self, other): # function to compare two circles radius
            if isinstance(other, Circle):
                return (self.radius == other.radius)
            return False