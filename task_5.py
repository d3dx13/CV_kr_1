import numpy as np

Image = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])
Image = np.random.randint(3, size=(5, 5))

hist, bins = np.histogram(Image.ravel(), 256, [0, 256])

res = {}

for i in range(256):
    if hist[i] != 0:
        res[i] = hist[i]
print("Image =")
print(Image)
print()
print("histogram =")
print(res)
print(f"else from {Image.min()} to {Image.max()} is 0")
