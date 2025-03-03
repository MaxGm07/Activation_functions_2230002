import numpy as np
import matplotlib.pyplot as plt

# Definir la función Sigmoid y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Aplicar la función Sigmoid y su derivada
y = sigmoid(x)
y_derivative = sigmoid_derivative(x)

# Graficar
def sigmoid_plot(ax):
    ax.plot(x, y, label="Sigmoid", color="red")
    ax.plot(x, y_derivative, label="Derivada de Sigmoid", color="orange", linestyle="--")
    ax.set_title("Función de Activación Sigmoid y su Derivada")
    ax.set_xlabel("x")
    ax.set_ylabel("Sigmoid(x)")
    ax.grid(True)
    ax.legend()

