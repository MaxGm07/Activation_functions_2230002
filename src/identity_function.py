import numpy as np
import matplotlib.pyplot as plt

# Definir la función Identidad y su derivada
def identity(x):
    return x

def identity_derivative(x):
    return np.ones_like(x)

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Aplicar la función Identidad y su derivada
y = identity(x)
y_derivative = identity_derivative(x)

# Se grafica la función Identidad y su derivada
def identity_plot(ax):
    ax.plot(x, y, label="Identidad", color="green")
    ax.plot(x, y_derivative, label="Derivada de Identidad", color="orange", linestyle="--")
    ax.set_title("Función de Activación Identidad")
    ax.set_xlabel("x")
    ax.set_ylabel("Identidad(x)")
    ax.grid(True)
    ax.legend()

