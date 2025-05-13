import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)   # 100 puntos entre 0 y 10
y = np.sin(x)

plt.plot(x, y)
plt.title("Seno de x")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()