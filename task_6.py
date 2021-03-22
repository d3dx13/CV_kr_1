import numpy as np
from scipy.ndimage.measurements import label

Image = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])
Image = np.random.randint(2, size=(5, 6))

structure4 = np.ones((3, 3), dtype=np.int)
structure4[0, 0] = 0
structure4[2, 2] = 0
structure4[2, 0] = 0
structure4[0, 2] = 0
structure8 = np.ones((3, 3), dtype=np.int)

print(structure4)
print(structure8)

labeled4, ncomponents4 = label(Image, structure4)
labeled8, ncomponents8 = label(Image, structure8)

print("Image =")
print(Image)
print()
print(f"По 4-связности = {ncomponents4}")
print(f"По 8-связности = {ncomponents8}")
print()
print(f"Матрица 4-связности = ")
print(labeled4)
print()
print(f"Матрица 8-связности = ")
print(labeled8)
