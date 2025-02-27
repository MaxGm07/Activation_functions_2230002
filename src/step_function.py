import numpy as np
import matplotlib.pyplot as plt

# Definir la función Escalón
def step(x):
    return np.where(x >= 0, 1, 0)

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Aplicar la función Escalón
y = step(x)

# Graficar
def step_plot(ax):
    ax.plot(x, y, label="Escalón", color="purple")
    ax.set_title("Función de Activación Escalón")
    ax.set_xlabel("x")
    ax.set_ylabel("Escalón(x)")
    ax.grid(True)
    ax.legend()
    