import numpy as np
import matplotlib.pyplot as plt


time = np.linspace(0, 10, 100)
money =time*2

plt.plot(time, money)
plt.title("Money over Time")
plt.xlabel("Time")
plt.ylabel("Money")
plt.show()