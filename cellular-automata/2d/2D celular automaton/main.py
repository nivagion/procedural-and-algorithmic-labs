import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation #class for animation
import numpy as np


SIZEX = 150
SIZEY = 150
GENERATIONS = 1000
#grid = np.zeros((SIZEX, SIZEY)) #numpy creates 2d grid of 0s
grid = np.random.choice([0, 1], size=(SIZEX, SIZEY), p=[0.8, 0.2]) #2D grid with random 0s and 1s 90% for 0 and 10% for 1


def rules(grid, rule): #for multiple rukles
    return rule(grid)

def rule1(grid): #CONWAYS GAME OF LIFE
    new_grid = np.zeros_like(grid) #numpy fills 2d grid with 0s
    for i in range(SIZEX):
        for j in range(SIZEY):
            total = np.sum(grid[max(i-1,0):min(i+2, SIZEX), max(j-1, 0):min(j+2, SIZEY)]) - grid[i,j] #how many neighbours, magic
            
            if grid[i, j] == 1:
                if total < 2 or total > 3: #underpopulation or overpopulation
                    new_grid[i, j] = 0
                else:
                    new_grid[i, j] = 1 #lives B)
            elif total == 3: #reproduction
                new_grid[i, j] = 1
    
    return new_grid

def rule2(grid):
    new_grid = np.zeros_like(grid)
    
    return new_grid


fig, ax = plt.subplots()

def update(i): #gets current frame
    ax.clear()
    global grid
    grid = rules(grid, rule1) #change for each rule
    ax.imshow(grid, cmap='binary')
    

animation = FuncAnimation(fig, update, frames=GENERATIONS, repeat=False, interval=50) #50 ms

plt.show()