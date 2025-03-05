import numpy as np
import matplotlib.pyplot as plt

# Definir la función Gaussiana y su derivada
def gaussian(x):
    return np.exp(-x**2)

def gaussian_derivative(x):
    return -2 * x * np.exp(-x**2)

# Crear un rango de valores para x
x = np.linspace(-5, 5, 1000)

# Aplicar la función Gaussiana y su derivada
y = gaussian(x)
y_derivative = gaussian_derivative(x)

# Se grafica la función Gaussiana y su derivada
def gaussian_plot(ax):
    ax.plot(x, y, label="Gaussiana", color="blue")
    ax.plot(x, y_derivative, label="Derivada de Gaussiana", color="orange", linestyle="--")
    ax.set_title("Función Gaussiana")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()
