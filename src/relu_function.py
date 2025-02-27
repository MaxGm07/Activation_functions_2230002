import numpy as np
import matplotlib.pyplot as plt

# Definir la función ReLU
def relu(x):
    return np.maximum(0, x)

# Crear un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Aplicar la función ReLU
y = relu(x)

# Graficar
def relu_plot(ax):
    ax.plot(x, y, label="ReLU", color="blue")
    ax.set_title("Función de Activación ReLU")
    ax.set_xlabel("x")
    ax.set_ylabel("ReLU(x)")
    ax.grid(True)
    ax.legend()
    

