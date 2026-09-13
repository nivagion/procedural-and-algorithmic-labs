import random
import numpy as np

def make_maze(w=16, h=8):
    # Create a grid with all walls
    maze = np.ones((h * 2 + 1, w * 2 + 1))

    # List of all cells
    cells = [(x, y) for x in range(w) for y in range(h)]

    for cell in cells:
        # Randomly choose to remove a vertical or horizontal wall
        if random.choice([True, False]):
            # Remove vertical wall
            if cell[0] > 0:
                maze[cell[1] * 2 + 1][cell[0] * 2] = 0
        else:
            # Remove horizontal wall
            if cell[1] > 0:
                maze[cell[1] * 2][cell[0] * 2 + 1] = 0

        # Carve a path in the maze
        maze[cell[1] * 2 + 1][cell[0] * 2 + 1] = 0

    return maze