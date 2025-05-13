import pandas as pd
import matplotlib.pyplot as plt



try:
	df = pd.read_csv("datos/notas.csv")
except FileNotFoundError:
	print("Error: The file 'datos/notas.csv' was not found.")
	exit()

required_columns = {"nombre", "parcial_1", "parcial_2", "final"}
if not required_columns.issubset(df.columns):
	print(f"Error: The file must contain the columns: {required_columns}")
	exit()

nombres = df["nombre"]
x = range(len(nombres))

plt.bar(x, df["parcial_1"], width=0.25, label="Parcial 1", align='center')
plt.bar([i + 0.25 for i in x], df["parcial_2"], width=0.25, label="Parcial 2", align='center')
plt.bar([i + 0.50 for i in x], df["final"], width=0.25, label="Final", align='center')

plt.xticks([i + 0.25 for i in x], nombres)
plt.title("Notas por estudiante")
plt.ylabel("Nota")
plt.legend()
plt.grid(True, axis='y')
plt.ylim(0, 5)
plt.show()