
def type_error(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")

def number_error(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")

class Rectangle:
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0):
        type_error(width, "width")
        type_error(height, "height") 
        type_error(x, "x") 
        type_error(y, "y") 

        number_error(width, "width")
        number_error(height, "height")
       
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def translate(self, dx: float, dy: float):
        self.x += dx
        self.y += dy
        print(f"new position: ({self.x}, {self.y})")

    @property
    def is_square(self) -> bool:
        return self.width == self.height

    def __str__(self):
        return f"Rectangle has size width={self.width}, height={self.height} and position x={self.x}, y={self.y}"
    def __repr__(self):
        return f"Rectangle:(width: {self.width}, height={self.height}, x:{self.x}, y:{self.y})"
   
    def __eq__(self, other):
            if isinstance(other, Rectangle):
                return (self.width == other.width and
                        self.height == other.height)
            return False 
    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area > other.area
        return False
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        return False
    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.area >= other.area
        return False
    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area <= other.area
        return False

   