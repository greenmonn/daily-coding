import numpy as np
from PIL import Image

arr = open("output", "rb").read() 

np_arr = np.frombuffer(arr, dtype=np.uint8)
np_arr = np.reshape(np_arr, (-1, 160))

grid = 16
size = int(160/grid)

def bytesToHexString(bytes):
        return ''.join(format(x, '02x') for x in bytes)

for i in range(grid):
    for j in range(grid):
                    
        cell = np_arr[size*i:size*(i+1), size*j:size*(j+1)]

        cell = cell.flatten()

        hex = bytesToHexString(cell)
        
        open("./cells/cell" + str(grid*i+j), "w").write(hex)