GRID_SIZE = 32, 32
FOOD_AMOUNT = 89
NUM_AGENTS = 100

class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """

    def __init__(self, width, height):
        """
        Create grid `array` width by height. Create a Grid object with
        a width, hieght, and array. Initially all locations hold None.
        """
        self.array = [[None for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height

    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        """
        if not self.in_bounds(x, y):
            raise IndexError(
                f"out of bounds get({x}, {y}) on grid width {self.width}, height {self.height}")

        return self.array[y][x]

    def set(self, x, y, val):
        if not self.in_bounds(x, y):
            raise IndexError(
                f"out of bounds set({x}, {y}, {val}) on grid width {self.width}, height {self.height}")

        self.array[y][x] = val

    def in_bounds(self, x, y):
        """Returns True if the (x, y) is in bounds of the grid. False otherwise."""
        return x >= 0 and x < self.width and y >= 0 and y < self.height
            
    def print_whole_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                print(f'{self.get(x,y)}, ')

    
