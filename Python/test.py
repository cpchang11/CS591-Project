import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2.5, 4, 6, 8]

plt.plot(x, y, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0, 10, 0, 10])
plt.show()

