import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os

sir = 3001
dub = 1500
a = [0] * sir

a[sir//2] = 1

b = [[0]*sir for _ in range(dub)]#lista visine dub i sirine sir

for i in range(sir):
    b[0][i] = a[i]

for i in range(dub):
    for j in range(sir):
        if i != dub -1:
            if j == 0:
                left = b[i][sir-1]
            else:
                left = b[i][j-1]
            if j == sir - 1:
                right = b[i][0]
            else:
                right = b[i][j+1]
            current = b[i][j]
            
            if left == 0 and current == 0 and right == 0:
                b[i + 1][j] = 0
            elif left == 0 and current == 0 and right == 1:
                b[i + 1][j] = 1
            elif left == 0 and current == 1 and right == 0:
                b[i + 1][j] = 1
            elif left == 0 and current == 1 and right == 1:
                b[i + 1][j] = 1
            elif left == 1 and current == 0 and right == 0:
                b[i + 1][j] = 1
            elif left == 1 and current == 0 and right == 1:
                b[i + 1][j] = 0
            elif left == 1 and current == 1 and right == 0:
                b[i + 1][j] = 0
            elif left == 1 and current == 1 and right == 1:
                b[i + 1][j] = 0

# Convert the list to a numpy array
data = np.array(b)

# Create a PIL image from the numpy array
img = Image.fromarray(np.uint8(data * 255) , 'L')

# Save the image
img.save('output.png')

