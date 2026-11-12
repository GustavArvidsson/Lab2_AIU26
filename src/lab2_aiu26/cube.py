from lab2_aiu26.shape3d import Shape3d, type_error, number_error

class Cube(Shape3d):
    def __init__(self, side_length: float, x: float = 0, y: float = 0, z: float = 0):
        super().__init__(x, y, z)
        type_error(side_length, "side_length")
        number_error(side_length, "side_length")
        self.side_length = side_length

    @property
    def volume(self):
        return self.side_length **3

    def __str__(self):
        return f"Cube has side length = {self.side_length} and position: x = {self.x}, y = {self.y}, z = {self.z}"

    def __repr__(self):
        return f"Cube:(side:length:{self.side_length}, x:{self.x}, y:{self.y}, z:{self.z})"

    def __eq__(self, other):
        if not isinstance(other, Cube):
            return self.side_length == other.side_length
        return False