import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

start = 0.0
stop = 6.0
c = 2.0
h = 0.01

# np.exp(x) == e**x
diff = lambda x, y: y + (np.exp(x) * (x**2 - 1))
f = lambda x: np.exp(x) * (c + ((x**3) / 3) - x)

def euler(x):
    y = c
    temp = start
    while temp < x:
        y = y + h * diff(temp, y)
        temp = temp + h
    return y

k1 = lambda x, y: h * diff(x, y)

k2x = lambda x: x + h/2
k2y = lambda x, y: (y + h * k1(x, y)) / 2
k2 = lambda x, y: h * diff(k2x(x), k2y(x, y))

k3x = lambda x: x + h
k3y = lambda x, y: y + 2*h*k2(x, y) - h*k1(x, y)
k3 = lambda x, y: h * diff(k3x(x), k3y(x, y))

def kutta(x):
    y = c
    temp = start
    while temp < x:
        y = y + h * diff(temp, y)
        k = k1(temp, y) + 4*k2(temp, y) + k3(temp, y)
        y = y + (k * h) /6
        temp = temp + h
    return y

ax = plt.axes()
# ax.set_ylim([-1, 5])

num = 1000
xPlot = np.linspace(start, stop, num)
fPlot = f(xPlot)
ax.plot(xPlot, fPlot)

ePlot = []
for i in range(0, num):
    ePlot.append(euler(xPlot[i]))
ax.plot(xPlot, ePlot)

kPlot = []
for i in range(0, num):
    kPlot.append(kutta(xPlot[i]))
ax.plot(xPlot, kPlot)

eErr = []
relEErr = []
kErr = []
relKErr = []
for i in range(0, num):
    eErr.append(fPlot[i] - ePlot[i])
    relEErr.append(np.abs(eErr[i]) / fPlot[i])

    kErr.append(fPlot[i] - kPlot[i])
    relKErr.append(np.abs(kErr[i]) / fPlot[i])

    # print(str(eErr[i]) + "     " + str(kErr[i]))

print("Euler: " + str(np.average(eErr)) + "   " + str(np.average(relEErr)))
print("Kutta: " + str(np.average(kErr)) + "   " + str(np.average(relKErr)))

plt.show()
