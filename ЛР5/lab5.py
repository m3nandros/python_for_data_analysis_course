import numpy as np

matrix = np.random.randint(-10, 10, (8, 8))
print(matrix)

print(matrix[3:7, 3:7])

min_elem = matrix.min()
mask = (matrix != min_elem).all(axis=1)
matrix = matrix[mask]
print(matrix)

min_row = np.full((1, matrix.shape[1]), min_elem)
matrix = np.vstack((min_row, matrix))
print(matrix)

matrix_sum = matrix.sum()
matrix_mean = matrix.mean()
print("Sum:", matrix_sum)
print("Mean:", matrix_mean)

names = np.array(['Вася', 'Коля', 'Петя', 'Вася', 'Коля'])
grades = np.array([[4, 5, 4, 3, 4, 5],
                    [2, 3, 4, 3, 2, 3],
                    [4, 4, 3, 3, 2, 3],
                    [5, 5, 5, 5, 4, 5],
                    [3, 3, 4, 3, 4, 5]])

name_to_find = 'Вася'
mask = (names == name_to_find)
print(grades[mask])

m1 = np.random.randint(1, 10, 10)
m2 = np.random.randint(1, 10, 10)

m3 = np.setxor1d(m1, m2)
mask = ((m1 % 3 == 0) | (m1 % 2 == 0))
m1[mask] = 1

m12 = np.concatenate((m1, m2))
matrix = m12.reshape(4, 5)
print(matrix)

matrix = np.delete(matrix, [0, 3], axis=1)
print(matrix)

matrix = matrix.T
print(matrix)

matrix = np.array([[0.54, 0.25, 0.2 ],
                    [0.3 , 0.17, 0.1 ],
                    [0.08, 0.06, 0.09]])

for col in range(1, matrix.shape[1]):
    if not np.allclose(matrix[:, col].sum(), matrix[:, col-1].sum()):
        # изменить некоторые элементы в этом столбце
        pass

det_a = np.linalg.det(matrix)

eye = np.eye(matrix.shape[0])
matrix_v = eye - matrix

matrix_c = np.linalg.inv(matrix_v)

vector_u = np.array([30, 17, 10])

vector_x = np.dot(matrix_c, vector_u)
vector_x = np.linalg.solve(np.eye(matrix.shape[0]) - matrix, vector_u)

x_points = np.array([1, 15])
y_points = np.array([np.sin(x_points[0] / 5) * np.exp(x_points[0] / 10) + 5 * np.exp(-x_points[0] / 2),
                      np.sin(x_points[1] / 5) * np.exp(x_points[1] / 10) + 5 * np.exp(-x_points[1] / 2)])

A = np.vstack((x_points, np.ones(x_points.shape))).T
b = y_points

from scipy.linalg import solve

w = solve(A, b)

import matplotlib.pyplot as plt

x_range = np.linspace(1, 15, 100)
y_range = np.sin(x_range / 5) * np.exp(x_range / 10) + 5 * np.exp(-x_range / 2)
poly_range = w[0] * x_range + w[1]

plt.plot(x_range, y_range, label='f(x)')
plt.plot(x_range, poly_range, label='poly(x)')
plt.legend()
plt.show()

x_points = np.array([1, 8, 15])
y_points = np.array([np.sin(x_points[0] / 5) * np.exp(x_points[0] / 10) + 5 * np.exp(-x_points[0] / 2),
                      np.sin(x_points[1] / 5) * np.exp(x_points[1] / 10) + 5 * np.exp(-x_points[1] / 2),
                      np.sin(x_points[2] / 5) * np.exp(x_points[2] / 10) + 5 * np.exp(-x_points[2] / 2)])

A = np.vstack((x_points**2, x_points, np.ones(x_points.shape))).T
b = y_points

w = solve(A, b)

x_range = np.linspace(1, 15, 100)
y_range = np.sin(x_range / 5) * np.exp(x_range / 10) + 5 * np.exp(-x_range / 2)
poly_range = w[0] * x_range**2 + w[1] * x_range + w[2]

plt.plot(x_range, y_range, label='f(x)')
plt.plot(x_range, poly_range, label='poly(x)')
plt.legend()
plt.show()

x_points = np.array([1, 4, 10, 15])
y_points = np.array([np.sin(x_points[0] / 5) * np.exp(x_points[0] / 10) + 5 * np.exp(-x_points[0] / 2),
                      np.sin(x_points[1] / 5) * np.exp(x_points[1] / 10) + 5 * np.exp(-x_points[1] / 2),
                      np.sin(x_points[2] / 5) * np.exp(x_points[2] / 10) + 5 * np.exp(-x_points[2] / 2),
                      np.sin(x_points[3] / 5) * np.exp(x_points[3] / 10) + 5 * np.exp(-x_points[3] / 2)])

A = np.vstack((x_points**3, x_points**2, x_points, np.ones(x_points.shape))).T
b = y_points

w = solve(A, b)

x_range = np.linspace(1, 15, 100)
y_range = np.sin(x_range / 5) * np.exp(x_range / 10) + 5 * np.exp(-x_range / 2)
poly_range = w[0] * x_range**3 + w[1] * x_range**2 + w[2] * x_range + w[3]

plt.plot(x_range, y_range, label='f(x)')
plt.plot(x_range, poly_range, label='poly(x)')
plt.legend()
plt.show()

with open('submission-2.txt', 'w') as f:
    f.write(' '.join(map(str, w)))

x_range = np.linspace(1, 15, 100)
y_range = np.sin(x_range / 5) * np.exp(x_range / 10) + 5 * np.exp(-x_range / 2)

poly_range_1 = w1[0] * x_range + w1[1]
poly_range_2 = w2[0] * x_range**2 + w2[1] * x_range + w2[2]
poly_range_3 = w3[0] * x_range**3 + w3[1] * x_range**2 + w3[2] * x_range + w3[3]

plt.plot(x_range, y_range, label='f(x)')
plt.plot(x_range, poly_range_1, label='poly_1(x)')
plt.plot(x_range, poly_range_2, label='poly_2(x)')
plt.plot(x_range, poly_range_3, label='poly_3(x)')
plt.legend()
plt.show()

with open('submission-2.txt', 'w') as f:
    f.write(' '.join(map(str, w)))

x_range = np.linspace(1, 15, 100)
y_range = np.sin(x_range / 5) * np.exp(x_range / 10) + 5 * np.exp(-x_range / 2)

poly_range_1 = w1[0] * x_range + w1[1]
poly_range_2 = w2[0] * x_range**2 + w2[1] * x_range + w2[2]
poly_range_3 = w3[0] * x_range**3 + w3[1] * x_range**2 + w3[2] * x_range + w3[3]

plt.plot(x_range, y_range, label='f(x)')
plt.plot(x_range, poly_range_1, label='poly_1(x)')
plt.plot(x_range, poly_range_2, label='poly_2(x)')
plt.plot(x_range, poly_range_3, label='poly_3(x)')
plt.legend()
plt.show()
