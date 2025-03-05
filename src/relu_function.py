import numpy as np
import matplotlib.pyplot as plt

# Definir la función ReLU y su derivada
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Aplicar la función ReLU y su derivada
y = relu(x)
y_derivative = relu_derivative(x)

# Se grafica la función ReLU y su derivada
def relu_plot(ax):
    ax.plot(x, y, label="ReLU", color="blue")
    ax.plot(x, y_derivative, label="Derivada de ReLU", color="orange", linestyle="--")
    ax.set_title("Función de Activación ReLU")
    ax.set_xlabel("x")
    ax.set_ylabel("ReLU(x)")
    ax.grid(True)
    ax.legend()
