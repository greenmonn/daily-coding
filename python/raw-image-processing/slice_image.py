import numpy as np
from PIL import Image

arr = open("output", "rb").read() 

np_arr = np.frombuffer(arr, dtype=np.uint8)
np_arr = np.reshape(np_arr, (160, 160))

grid = 10
size = int(160/grid)

for i in range(grid):
    for j in range(grid):
        cell = np_arr[size*j:size*(j+1), size*i:size*(i+1)]
        cell = np.reshape(cell, (size*size))
        
        open("./cells/cell" + str(grid*i+j), "wb").write(cell)