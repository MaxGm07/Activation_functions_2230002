import numpy as np
import matplotlib.pyplot as plt

# Definir la función Identidad
def identity(x):
    return x

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Aplicar la función Identidad
y = identity(x)

# Graficar
def identity_plot(ax):
    ax.plot(x, y, label="Identidad", color="green")
    ax.set_title("Función de Activación Identidad")
    ax.set_xlabel("x")
    ax.set_ylabel("Identidad(x)")
    ax.grid(True)
    ax.legend()
    