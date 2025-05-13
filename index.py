
import matplotlib.pyplot as plt

# Datos
etiquetas = ['Manzanas', 'Bananas', 'Cerezas', 'Uvas']
valores = [30, 25, 20, 25]
colores = ['red', 'yellow', 'pink', 'purple']

# Crear el gráfico de pastel
plt.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Frutas')
plt.axis('equal')  # Hace que el gráfico sea un círculo perfecto

# Mostrar
plt.show()
