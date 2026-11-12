def type_error(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number") 

def number_error(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")

class Shape3d:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        type_error(x,"x")
        type_error(y, "y")
        type_error(z, "z")

        self.x = x
        self.y = y
        self.z = z

    def translate(self, dx: float, dy: float, dz: float):
        type_error(dx, "dx")
        type_error(dy, "dy")
        type_error(dz, "dz")

        self.x += dx
        self.y += dy
        self.z += dz

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

