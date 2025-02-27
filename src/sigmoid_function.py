import numpy as np
import matplotlib.pyplot as plt

# Definir la función Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Aplicar la función Sigmoid
y = sigmoid(x)

# Graficar
def sigmoid_plot(ax):
    ax.plot(x, y, label="Sigmoid", color="red")
    ax.set_title("Función de Activación Sigmoid")
    ax.set_xlabel("x")
    ax.set_ylabel("Sigmoid(x)")
    ax.grid(True)
    ax.legend()
    