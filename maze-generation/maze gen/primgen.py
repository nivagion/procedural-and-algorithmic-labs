import random
import numpy as np

def make_maze(w=16, h=8):
    # Create a grid with all walls
    maze = np.ones((h * 2 + 1, w * 2 + 1))

    # List of all cells
    cells = [(x, y) for x in range(w) for y in range(h)]

    # Start with a random cell
    start = random.choice(cells)
    cells.remove(start)

    # List of visited cells
    visited = [start]

    while cells:
        # Pick a random visited cell and a random neighbor
        cell = random.choice(visited)
        neighbors = [(cell[0] + dx, cell[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] if (cell[0] + dx, cell[1] + dy) in cells]

        if not neighbors:
            # If the cell has no unvisited neighbors, remove it from the list
            visited.remove(cell)
            continue

        # Choose a random neighbor and remove the wall between the cell and the neighbor
        neighbor = random.choice(neighbors)
        maze[cell[1] * 2 + 1 + (neighbor[1] - cell[1])][cell[0] * 2 + 1 + (neighbor[0] - cell[0])] = 0

        # Mark the neighbor as visited
        cells.remove(neighbor)
        visited.append(neighbor)

        # Carve a path in the maze
        maze[neighbor[1] * 2 + 1][neighbor[0] * 2 + 1] = 0

    return maze