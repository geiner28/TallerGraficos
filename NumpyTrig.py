import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)

plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.legend()
plt.title("Funciones trigonométricas")
plt.grid(True)
plt.show()