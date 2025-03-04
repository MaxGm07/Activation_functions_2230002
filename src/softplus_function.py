import numpy as np
import matplotlib.pyplot as plt

# Definir la función Softplus y su derivada
def softplus(x):
    return np.log1p(np.exp(x))  # log1p es más estable numéricamente para log(1 + x)

def softplus_derivative(x):
    return 1 / (1 + np.exp(-x))  # Derivada es la función sigmoid

# Graficar
def softplus_plot(ax):
    x = np.linspace(-10, 10, 1000)
    y = softplus(x)
    y_derivative = softplus_derivative(x)
    ax.plot(x, y, label="Softplus", color="magenta")
    ax.plot(x, y_derivative, label="Derivada de Softplus", color="orange", linestyle="--")
    ax.set_title("Función Softplus y su Derivada")
    ax.set_xlabel("x")
    ax.set_ylabel("Softplus(x)")
    ax.grid(True)
    ax.legend()