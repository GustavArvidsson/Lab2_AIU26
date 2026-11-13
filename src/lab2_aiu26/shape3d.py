def type_error(value, name): #checks if the value is a number
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number") 

def number_error(value, name): #checks if the value is greater than zero
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")

class Shape3d:# base class for all 3d shapes
    def __init__(self, x: float = 0, y: float = 0, z: float = 0): #Function to initialize 3d shapes with a position
        type_error(x,"x")
        type_error(y, "y")
        type_error(z, "z")

        self.x = x
        self.y = y
        self.z = z

    def translate(self, dx: float, dy: float, dz: float): #Function to move 3d shapes on x, y and z axis
        type_error(dx, "dx")
        type_error(dy, "dy")
        type_error(dz, "dz")

        self.x += dx
        self.y += dy
        self.z += dz

    #functions to compare 3d shapes based on volume
    def __gt__(self, other) -> bool: 
        if not isinstance(other, Shape3d):
            return NotImplemented
        return self.volume > other.volume

    def __lt__(self, other) -> bool:
        if not isinstance(other, Shape3d):
            return NotImplemented
        return self.volume < other.volume

    def __le__(self, other) -> bool:
        if not isinstance(other, Shape3d):
            return NotImplemented
        return self.volume <= other.volume

    def __ge__(self, other) -> bool:
        if not isinstance(other, Shape3d):
            return NotImplemented
        return self.volume >= other.volume

