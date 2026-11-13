
def type_error(value, name): #checks if the value is a number
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")

def number_error(value, name): #checks if the value is greater than zero
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")

class Shape: #base class for all 2d shapes
    def __init__(self, x: float = 0, y: float = 0):
        type_error(x,"x")
        type_error(y, "y")

        self.x = x
        self.y = y

    def translate(self, dx: float, dy: float): #Function to move 2d shapes on x and y axis
        type_error(dx, "dx")
        type_error(dy, "dy")

        self.x += dx
        self.y += dy

    #functions to compare 2d shapes based on area
    def __gt__(self, other) -> bool: 
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area > other.area

    def __lt__(self, other) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area < other.area
       
    def __le__(self, other) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area <= other.area

    def __ge__(self, other) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area >= other.area