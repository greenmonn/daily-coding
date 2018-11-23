from PIL import Image

import numpy as np

arr = open("cells/cell93", "rb").read() 

np_arr = np.frombuffer(arr, dtype=np.uint8)

np_arr = np.reshape(np_arr, (16, 16))

print(np_arr)

img = Image.fromarray(np_arr)

img.show()