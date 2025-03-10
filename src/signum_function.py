import numpy as np
import matplotlib.pyplot as plt

# Define the Signum function and its derivative
def signum(x):
    return np.where(x < 0, -1, np.where(x > 0, 1, 0))

def signum_derivative(x):
    return np.zeros_like(x)  # Derivative is 0 everywhere except at x=0

# Plot the Signum function and its derivative
def signum_plot(ax):
    x = np.linspace(-10, 10, 1000)
    y = signum(x)
    y_derivative = signum_derivative(x)
    ax.plot(x, y, label="Signum", color="purple")
    ax.plot(x, y_derivative, label="Derivada de Signum", color="orange", linestyle="--")
    ax.set_title("Función Signum")
    ax.set_xlabel("x")
    ax.set_ylabel("Signum(x)")
    ax.grid(True)
    ax.legend()