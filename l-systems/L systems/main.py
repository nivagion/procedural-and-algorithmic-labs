import matplotlib.pyplot as plt
import numpy as np

#rules = {'F': 'FF', 'X': 'F-[[X]+X]+F[+FX]-X'}
#start_string = 'X'

#rules = {'F': 'FF', 'X': 'F+[[X]-X]-F[-FX]+X'}
#start_string = 'X'


#L-system rules for a fractal tree
rules = {'F': 'FF', 'X': 'F[+X][-X]+X'}

#starting string
start_string = 'X'

angle = 28

#number of iterations
iterations = 12


lsystem_string = start_string
for _ in range(iterations):
    lsystem_string = ''.join([rules.get(char, char) for char in lsystem_string])

x, y, direction = 0, 0, 0

#store the x and y coordinates
x_coords, y_coords = [x], [y]

#parse  L-system string and update the turtle's position and direction
for char in lsystem_string:
    if char == 'F':
        x += np.cos(np.radians(direction))
        y += np.sin(np.radians(direction))
        x_coords.append(x)
        y_coords.append(y)
    elif char == '+':
        direction += angle
    elif char == '-':
        direction -= angle

#plot the L-system
plt.figure(figsize=(10, 10))
plt.plot(x_coords, y_coords)
plt.axis('off')
plt.show()
