import numpy as np
import time
import random
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def first():
    l1 = [random.randint(-100, 100) for i in range(10**6)]
    l2 = [random.randint(-100, 100) for i in range(10**6)]

    t_start = time.perf_counter()
    l3 = [l1[i] * l2[i] for i in range(10**6)]
    print(time.perf_counter() - t_start)

    l1 = np.array(l1)
    l2 = np.array(l2)

    t_start = time.perf_counter()
    l3 = np.multiply(l1, l2)
    print(time.perf_counter() - t_start)

def second():
    data = []

    with open('data2.csv') as f:
        reader = csv.reader(f, delimiter=",")

        for s in reader:
            data.append(s[1])
        data = data[1:]
        data = list(map(float, data))

    data = np.array(data)

    plt.hist(data, 32)
    plt.title('Гистограмма')
    plt.xlabel('Hardness')
    plt.ylabel('Частота')
    plt.show()

    plt.hist(data, 32, density=True)
    plt.title('Нормализованная гистограмма')
    plt.xlabel('Hardness')
    plt.ylabel('Частота')
    plt.show()

    print(f'Среднеквадратичное отклонение: {np.std(data)}')

def third():
    x = np.linspace(0, 5, 100) # поставил интервал от 0 до 5 т.к. z степенная функция
    y = x
    z = np.sin(x ** y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    plt.show()

def dop():
    fig, ax = plt.subplots()
    line, = plt.plot([], [])
    ax = plt.axis([0, 2 * np.pi, -1, 1])
    x = []
    y = []

    def func(i):
        x.append(i)
        y.append(np.sin(i))
        line.set_data(x, y)

    _animation = FuncAnimation(fig, func, frames=np.arange(0, 2 * np.pi, 0.1), repeat=False)
    plt.show()

first()
second()
third()
dop()

