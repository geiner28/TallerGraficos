#Escribe un programa que grafique la siguiente lista de valores: valores = [3, 7, 1, 5, 12] Agrega título, etiquetas de ejes y una cuadrícula

from matplotlib import pyplot as plt
import numpy as np


valores = [3, 7, 1, 5, 12]
x = np.arange(len(valores))
# Crear el gráfico de línea
plt.plot(x, valores, marker='o', color='blue')
plt.title('Gráfico de Línea Simple')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.savefig("./Graficos/grafica_linea.png")




#Gráfico de barras Grafica la cantidad de estudiantes en 5 cursos:
cursos = ['A', 'B', 'C', 'D', 'E']
cantidad = [30, 25, 40, 20, 35]
# Crear el gráfico de barras
plt.bar(cursos, cantidad, color='green')
plt.title('Cantidad de Estudiantes por Curso')
plt.xlabel('Cursos')
plt.ylabel('Cantidad de Estudiantes')
plt.grid(axis='y')
plt.savefig("Graficos/grafica_cursos.png")
plt.show()

#Gráfico de dispersión (scatter plot) Genera dos listas de números aleatorios de 50 elementos y haz un gráfico de dispersión.

import random
x = [random.randint(1, 100) for _ in range(50)]
y = [random.randint(1, 100) for _ in range(50)]
# Crear el gráfico de dispersión
plt.scatter(x, y, color='red')
plt.title('Gráfico de Dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.savefig("Graficos/grafica_dispersion.png")
plt.show()

#Subplots Crea un figure con 2 subgráficos:
# Uno con una línea senoidal.
# Otro con una función cuadrática

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = x ** 2
# Crear la figura y los subgráficos
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
# Gráfico de la función senoidal
ax1.plot(x, y1, color='purple')
ax1.set_title('Función Senoidal')
ax1.set_xlabel('Eje X')
ax1.set_ylabel('Seno')
ax1.grid(True)
# Gráfico de la función cuadrática
ax2.plot(x, y2, color='orange') 
ax2.set_title('Función Cuadrática')
ax2.set_xlabel('Eje X')
ax2.set_ylabel('Cuadrado')
ax2.grid(True)
plt.tight_layout()
plt.savefig("Graficos/grafica_subplots.png")
plt.show()



"""Parte 2: Cálculos y gráficos con NumPy (4 ejercicios)
5. Generar datos y graficar una función
Usa np.linspace() para generar valores x entre -10 y 10, y grafica y = x² - 3x + 2."""

x = np.linspace(-10, 10, 100)
y = x ** 2 - 3 * x + 2
# Crear el gráfico
plt.plot(x, y, color='blue')
plt.title('Gráfico de la función y = x² - 3x + 2')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)
plt.savefig("Graficos/grafica_funcion.png")
plt.show()  



"""6. Comparación de funciones
En el mismo gráfico, traza las funciones sin(x) y cos(x) para x entre 0 y 2π"""

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# Crear el gráfico
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='orange')
plt.title('Comparación de funciones')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()
plt.grid(True)
plt.savefig("Graficos/grafica_comparacion.png")
plt.show()


""""7. Operaciones entre arrays
Genera dos vectores de 100 valores aleatorios entre 0 y 100 y calcula:
• La suma total.
• El valor máximo.
• La desviación estándar."""


# Generar dos vectores de 100 valores aleatorios entre 0 y 100
vector1 = np.random.randint(0, 100, 100)
vector2 = np.random.randint(0, 100, 100)
# Calcular la suma total
suma_total = np.sum(vector1 + vector2)
# Calcular el valor máximo
maximo = np.max(vector1 + vector2)
# Calcular la desviación estándar
desviacion_estandar = np.std(vector1 + vector2)
# Mostrar resultados
print(f"Suma total: {suma_total}")
print(f"Valor máximo: {maximo}")
print(f"Desviación estándar: {desviacion_estandar}")



"""8. Histograma con NumPy
Genera 1000 números aleatorios con distribución normal y muestra un histograma con
plt.hist()."""

# Generar 1000 números aleatorios con distribución normal
numeros_aleatorios = np.random.normal(loc=0, scale=1, size=1000)
# Crear el histograma
plt.hist(numeros_aleatorios, bins=30, color='blue', alpha=0.7)
plt.title('Histograma de Números Aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')    
plt.grid(axis='y')
plt.savefig("Graficos/grafica_histograma.png")
plt.show()




import pandas as pd
# Cargar el archivo
df = pd.read_csv("datos/datos_ventas.csv")
# Mostrar las primeras 5 filas
print(df.head())




""""10. Estadísticas básicas
Muestra:
• Total de ventas (Ventas.sum())
• Promedio de precio
• Producto más vendido"""

# Total de ventas
total_ventas = df['Ventas'].sum()
# Promedio de precio
promedio_precio = df['Precio'].mean()
# Producto más vendido
producto_mas_vendido = df.loc[df['Ventas'].idxmax(), 'Producto']
# Mostrar resultados
print(f"Total de ventas: {total_ventas}")
print(f"Promedio de precio: {promedio_precio}") 
print(f"Producto más vendido: {producto_mas_vendido}")



"""""11. Filtrar datos
Muestra solo los productos vendidos en el mes de enero (Fecha empieza por 2025-01)"""

