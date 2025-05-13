import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y = np.exp(-x/3) * np.sin(2 * x)

plt.plot(x, y, color='purple', linestyle='--', marker='o')
plt.title("Gráfico con NumPy")
plt.show()