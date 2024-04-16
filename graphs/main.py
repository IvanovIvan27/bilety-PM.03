import matplotlib.pyplot as plt
import numpy as np

# Чтение коэффициентов и шага сетки из файла
with open('input.txt', 'r') as file:
    a, b, c, step = map(float, file.readline().split())

# Определение диапазона для построения графика
x = np.arange(-10, 10, step * 0.2)
y = a / (b * x + c)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('График функции y = a / (b * x + c)')
plt.grid(True)
plt.show()
