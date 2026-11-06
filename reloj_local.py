# Reloj de la clase 1, ahora en tu computador
# Guarda este archivo en la misma carpeta que ventas_trimestre.xlsx

# %% Cargar los datos
import pandas as pd
import matplotlib.pyplot as plt  # fuera de Colab, se necesita para mostrar gráficos

ventas = pd.read_excel("ventas_trimestre.xlsx")
print("Datos listos:", len(ventas), "pedidos")

# %% Elegir el país
pais = "Perú"
seleccion = ventas[ventas["pais"] == pais]
filas, columnas = seleccion.shape
print(pais, "·", filas, "pedidos · total neto:", seleccion["total"].sum())

# %% Gráfico por categoría
seleccion["categoria"].value_counts().plot(kind="bar", title="Pedidos en " + pais + " por categoría")
plt.tight_layout()
plt.show()
