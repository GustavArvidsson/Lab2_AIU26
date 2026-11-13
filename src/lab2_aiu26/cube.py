from lab2_aiu26.shape3d import Shape3d, type_error, number_error

class Cube(Shape3d): # class for creating a cube
    def __init__(self, side_length: float, x: float = 0, y: float = 0, z: float = 0):
        super().__init__(x, y, z)
        type_error(side_length, "side_length")
        number_error(side_length, "side_length")
        self.side_length = side_length

    @property # property to calculate volume 
    def volume(self):
        return self.side_length **3

    def __str__(self): #function to display the cube object
        return f"Cube has side length = {self.side_length} and position: x = {self.x}, y = {self.y}, z = {self.z}"

    def __repr__(self): # function to display the cube object in a more detailed way
        return f"Cube:(side:length:{self.side_length}, x:{self.x}, y:{self.y}, z:{self.z})"

    def __eq__(self, other): #function to compare to two cube objects baed on its side length
        if not isinstance(other, Cube):
            return self.side_length == other.side_length
        return False