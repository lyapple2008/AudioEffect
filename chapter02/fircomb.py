import numpy as np
import matplotlib.pyplot as plt

x = np.zeros((100, 1))
x[0] = 1
g = 0.5
T = 10
Delayline = np.zeros((T, 1))
y = np.zeros((100, 1))


for i in np.arange(x.size):
    y[i] = x[i] + g * Delayline[T-1]
    Delayline = np.append(x[i], Delayline[:T-1])

plt.subplot(2, 1, 1)
plt.plot(np.arange(100), x, 'r')
plt.subplot(2, 1, 2)
plt.plot(np.arange(100), y, 'g')
plt.show()