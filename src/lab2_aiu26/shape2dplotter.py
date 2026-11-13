import matplotlib.pyplot as plt
from matplotlib.patches import Circle as CirclePatch
from matplotlib.patches import Rectangle as RectanglePatch


class Shape2dPlotter: #class for plotting 2D shapes using matplotlib
    def __init__(self): #initialize the plotter with a figure and axis
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal")
        self.ax.grid(True)
        self.ax.axhline(y=0, color="black", linewidth=1)
        self.ax.axvline(x=0, color="black", linewidth=1)   


    def add_circle(self, circle, label, color):# function to add a circle to the plot with a label and color
        patch = CirclePatch((circle.x, circle.y), radius=circle.radius, fill=False, label=label, edgecolor=color)
        self.ax.add_patch(patch)
        self.ax.legend()

    def add_rectangle(self, rectangle, label, color): # function to add a rectangle to the plot with a label and color
        patch = RectanglePatch(
        (rectangle.x - rectangle.width / 2, rectangle.y - rectangle.height / 2), width=rectangle.width, height=rectangle.height, fill=False, label=label, edgecolor=color)
        self.ax.add_patch(patch)
        self.ax.legend()
    def show(self) -> None:
        plt.show()