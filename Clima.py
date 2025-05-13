import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv("datos/clima.csv")  # Asegúrate de guardar los datos en un archivo con este nombre

# Mostrar las primeras filas
print("Datos:")
print(data)

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(data.describe())

# Temperatura media
temp_media = np.mean(data["temperatura"])
print(f"\nTemperatura media: {temp_media:.2f} °C")

# Lluvia total
lluvia_total = np.sum(data["lluvia"])
print(f"Lluvia total de la semana: {lluvia_total} mm")

# Gráfico de temperatura por día
plt.figure(figsize=(10, 5))
plt.plot(data["dia"], data["temperatura"], marker='o', color='orange')
plt.title("Temperatura diaria")
plt.xlabel("Día")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.show()

# Gráfico de lluvia por día
plt.figure(figsize=(10, 5))
plt.bar(data["dia"], data["lluvia"], color='blue')
plt.title("Lluvia por día")
plt.xlabel("Día")
plt.ylabel("Lluvia (mm)")
plt.grid(axis='y')
plt.show()