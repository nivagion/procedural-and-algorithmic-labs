import random #maybe add "solvable check"
import matplotlib.pyplot as plt
import numpy as np
import dfsgen as dfs
import primgen as prm
import randlinegen as rlg

WhatToDo = 'b'
WhatToDo = input("DFS-d, prim-p, random-r,  ")

if WhatToDo == 'd':
    maze = dfs.make_maze(30,30)
    plt.imshow(maze, cmap='binary')
    plt.title('Depth-first search generation')
    plt.show()
elif WhatToDo == 'p':
    maze = prm.make_maze(30,30)
    plt.imshow(maze, cmap='binary')
    plt.title('Prim\'s algorithm generation')
    plt.show()
elif WhatToDo == 'r':
    maze = rlg.make_maze(30,30)
    plt.imshow(maze, cmap='binary')
    plt.title('Random line generation')
    plt.show()
elif WhatToDo == '':
    pass