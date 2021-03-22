import numpy as np

Image = np.array([
[1, 2, 3, 4, 5],
[1, 2, 3, 4, 5],
[1, 2, 3, 4, 5],
[1, 2, 3, 4, 5],
[1, 2, 3, 4, 5]
])
Image = np.random.randint(256, size=(5,5))

hist,bins = np.histogram(Image.ravel(),256,[0,256])

res = {}

for i in range(256):
    if hist[i] != 0:
        res[i] = hist[i]
print("Image =")
print(Image)
print()
print("histogram =")
print(res)
print("else 0")

