import numpy as np

Image = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])
Image = np.random.randint(256, size=(5, 5))

Mask = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])
Mask = np.random.randint(2, size=(5, 5))

Res = np.multiply(Image, Mask)

print("Image =")
print(Image)
print()
print("Image =")
print(Mask)
print()
print("Res =")
print(Res)
print()
