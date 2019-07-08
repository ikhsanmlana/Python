import numpy as np
import matplotlib.pyplot as plt

def equation(t0, y):
    return (y*(t0)**3) - (1.5 * y)

def exact1(t):
    return np.exp(t**4/4 - 1.5*t)

def plot1(x, y, exact):
    plt.plot(x, y)
    plt.xlabel("t0")
    plt.ylabel("y")
    plt.plot(x, exact)
    plt.gca().legend(("Estimate", "Exact"))
    plt.show()

def euler(y, t, h):
    loop = int(t / h)
    t0 = 0
    y1 = y
    plot_y = []
    plot_y.append(y)
    plot_x = []
    plot_x.append(t0)
    plot_exact = [y]
    for i in range(loop):
        y1 = y1 + (equation(t0, y1) * h)
        t0 = t0 + h
        plot_y.append(y1)
        plot_x.append(t0)
        plot_exact.append(exact1(t0))
    if h == 0.5:
        plt.title("Euler Method when h = 0.5")
    elif h == 0.25:
        plt.title("Euler Method when h = 0.25")
    plot1(plot_x, plot_y, plot_exact)
    return y1

def heun(y, t, h):
    loop = int(t / h)
    t0 = 0
    y1 = y
    plot_y = []
    plot_y.append(y)
    plot_x = []
    plot_x.append(t0)
    plot_exact = [y]
    for i in range(loop):
        k1 = equation(t0, y1)
        k2 = equation(t0 + h, (y1 + (k1 * h)))
        y1 = y1 + (((0.5 * k1) + (0.5 * k2)) * h)
        t0 = t0 + h
        plot_y.append(y1)
        plot_x.append(t0)
        plot_exact.append(exact1(t0))
    if h == 0.5:
        plt.title("Heeun Method when h = 0.5")
    elif h == 0.25:
        plt.title("Heeun Method when h = 0.25")
    plot1(plot_x, plot_y, plot_exact)
    return y1


def rk4(y, t, h):
    loop = int(t / h)
    t0 = 0
    y1 = y
    plot_y = [y]
    plot_x = [t0]
    plot_exact = [1]
    for i in range(loop):
        k1 = equation(t0, y1)
        k2 = equation(t0 + (0.5*h), (y1 + (0.5*(k1 * h))))
        k3 = equation(t0 + (0.5*h), (y1 + (0.5*(k2 * h))))
        k4 = equation(t0 + h, (y1 + (k3 * h)))
        y1 = y1 + ((1/6*(k1 + 2*k2 + 2*k3 + k4)) * h)
        t0 = t0 + h
        plot_y.append(y1)
        plot_x.append(t0)
        plot_exact.append(exact1(t0))
    if h == 0.5:
        plt.title("Runge-Kutta 4th Method when h = 0.5")
    elif h == 0.25:
        plt.title("Runge-Kutta 4th Method when h = 0.25")
    plot1(plot_x, plot_y, plot_exact)
    return y1

exact = 2.7183

print("Estimation error for euler (h = 0.5): " , (( exact - euler(1, 2, 0.5)) / exact ) * 100 )
print("Estimation error for euler (h = 0.25): " , (( exact - euler(1, 2, 0.25)) / exact ) * 100 )

print("Estimation error for heun (h = 0.5): " , (( exact - heun(1, 2, 0.5)) / exact ) * 100 )
print("Estimation error for heun (h = 0.25): " , (( exact - heun(1, 2, 0.25)) / exact ) * 100 )

print("Estimation error for Runge-Kutta 4th  (h = 0.5): " , (( exact - rk4(1, 2, 0.5)) / exact ) * 100 )
print("Estimation error for Runge-Kutta 4th (h = 0.25): " , (( exact - rk4(1, 2, 0.25)) / exact ) * 100 )


