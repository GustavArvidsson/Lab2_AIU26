import math
from .shape import Shape, type_error, number_error



class Rectangle(Shape): # Class for creating rectangles
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0):
        super().__init__(x,y)
        type_error(width, "width")
        type_error(height, "height") 

        number_error(width, "width")
        number_error(height, "height")
       
        self.width = width
        self.height = height
       
    @property # read only property for calculating area
    def area(self) -> float:
        return self.width * self.height

    @property # read only property for calculating perimeter
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


    def rotate_90(self) -> None:
        self.width, self.height = self.height, self.width


    def is_square(self) -> bool: #function to check if a rectangle is unit
        return self.width == self.height

    def __str__(self): #function to display the rectangle object
        return f"Rectangle has size width={self.width}, height={self.height} and position x={self.x}, y={self.y}"
    def __repr__(self):#function to display the rectangle object in a more detailed way
        return f"Rectangle:(width: {self.width}, height={self.height}, x:{self.x}, y:{self.y})"
   
    def __eq__(self, other): #function to compare two rectangles objects based on their height and width
            if isinstance(other, Rectangle):
                return (self.width == other.width and
                        self.height == other.height)
            return False 
   