import numpy as np
import matplotlib.pyplot as plt

# Define the Identity function and its derivative
def identity(x):
    return x

def identity_derivative(x):
    return np.ones_like(x)

# Create a range of values for x
x = np.linspace(-10, 10, 1000)

# Apply the Identity function and its derivative
y = identity(x)
y_derivative = identity_derivative(x)

# Plot the Identity function and its derivative
def identity_plot(ax):
    ax.plot(x, y, label="Identidad", color="green")
    ax.plot(x, y_derivative, label="Derivada de Identidad", color="orange", linestyle="--")
    ax.set_title("Función de Activación Identidad")
    ax.set_xlabel("x")
    ax.set_ylabel("Identidad(x)")
    ax.grid(True)
    ax.legend()

