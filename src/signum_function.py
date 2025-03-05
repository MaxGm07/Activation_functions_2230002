import numpy as np
import matplotlib.pyplot as plt

# Definir la función Signum y su derivada
def signum(x):
    return np.where(x < 0, -1, np.where(x > 0, 1, 0))

def signum_derivative(x):
    return np.zeros_like(x)  # Derivada es 0 en todas partes excepto en x=0

# Se grafica la función Signum y su derivada
def signum_plot(ax):
    x = np.linspace(-10, 10, 1000)
    y = signum(x)
    y_derivative = signum_derivative(x)
    ax.plot(x, y, label="Signum", color="k")
    ax.plot(x, y_derivative, label="Derivada de Signum", color="orange", linestyle="--")
    ax.set_title("Función Signum")
    ax.set_xlabel("x")
    ax.set_ylabel("Signum(x)")
    ax.grid(True)
    ax.legend()