import numpy as np
import matplotlib.pyplot as plt

# Definir la función Escalón y su derivada
def step(x):
    return np.where(x >= 0, 1, 0)

def step_derivative(x):
    return np.zeros_like(x)  # Derivada es 0 en todas partes excepto en x=0

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Aplicar la función Escalón y su derivada
y = step(x)
y_derivative = step_derivative(x)

# Se grafica la función Step (Escalón) y su derivada
def step_plot(ax):
    ax.plot(x, y, label="Escalón", color="purple")
    ax.plot(x, y_derivative, label="Derivada de Escalón", color="orange", linestyle="--")
    ax.set_title("Función de Activación Escalón")
    ax.set_xlabel("x")
    ax.set_ylabel("Escalón(x)")
    ax.grid(True)
    ax.legend()

