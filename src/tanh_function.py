import numpy as np
import matplotlib.pyplot as plt

# Definir la función Tangente Hiperbólica y su derivada
def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x)**2

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Aplicar la función Tangente Hiperbólica y su derivada
y = tanh(x)
y_derivative = tanh_derivative(x)

# Se grafica la función Tangente Hiperbólica y su derivada
def tanh_plot(ax):
    ax.plot(x, y, label="Tangente Hiperbólica", color="purple")
    ax.plot(x, y_derivative, label="Derivada de Tangente Hiperbólica", color="orange", linestyle="--")
    ax.set_title("Función Tangente Hiperbólica")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()

