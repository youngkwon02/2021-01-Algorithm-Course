import numpy as np

def matrixRotation(original):
    new_matrix = np.zeros((5, 5), dtype=np.int16)
    for i in range(0, 5):
        for k in range(0, 5):
            new_matrix[i, k] = original[4 - k, i]
    return new_matrix

org_matrix = np.random.randint(0, 256, size=(5, 5))
print("Random initial matrix:")
print(org_matrix)
print("\nRoatated matrix:")
new_matrix = matrixRotation(org_matrix)
print(new_matrix)