import random#DFS
import matplotlib.pyplot as plt
import numpy as np

def make_maze(w=30, h=30):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        random.shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(random.randrange(w), random.randrange(h))

    #visualize using matplotlib
    maze = np.zeros((h * 2 + 1, w * 2 + 1))
    for y in range(h):
        for x in range(w):
            maze[y * 2 + 1][x * 2 + 1] = 1
            if hor[y][x] == "+  ":
                maze[y * 2 + 2][x * 2 + 1] = 1
            if ver[y][x] == "   ":
                maze[y * 2 + 1][x * 2 + 2] = 1

    return maze
#print(make_maze())