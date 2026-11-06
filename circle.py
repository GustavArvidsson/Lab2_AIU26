import math


def type_error(value, name):
     if not isinstance(value, (int, float)):
          raise TypeError(f"{name} must be a number")

def number_error(value, name):
     if value <= 0:
          raise ValueError(f"{name} must be grater than zero")
     
class Circle:
    def __init__(self, radius: float, x: float = 0, y: float = 0):
          type_error(radius, "radius")
          number_error(radius, "radius")
          type_error(x, "x")
          type_error(y, "y")
          self.radius = radius
          self.x = x
          self.y = y
        
    @property
    def area(self) -> float:
        return math.pi * self.radius ** 2

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    @property
    def is_circle_unit(self) -> bool:
         return self.radius == 1

    def translate(self, dx: float, dy: float):
        type_error(dx, "x")
        type_error(dy, "y")
        
        self.x += dx
        self.y += dy

    def __str__(self):
         return f"Circle has radius = {self.radius} and position: x = {self.x}, y = {self.y}"
    def __repr__(self):
         return f"Circle:(radius:{self.radius}, x:{self.x}, y:{self.y})"


    def __eq__(self, other):
            if isinstance(other, Circle):
                return (self.radius == other.radius)
            return False
    def __gt__(self, other):
        if isinstance(other, Circle):
             return(self.radius > other.radius)
        return False
    def __lt__(self, other):
         if isinstance(other, Circle):
              return(self.radius < other.radius)
         return False
    def __ge__(self, other):
         if isinstance(other, Circle):
              return(self.radius >= other.radius)
         return False