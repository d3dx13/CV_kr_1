import numpy as np

Image = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])
Image = np.random.randint(3, size=(5, 5))

Used = np.zeros(Image.shape)

print(Used)
