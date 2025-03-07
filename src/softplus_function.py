import numpy as np
import matplotlib.pyplot as plt

# Define the Softplus function and its derivative
def softplus(x):
    return np.log1p(np.exp(x))  # log1p is numerically more stable for log(1 + x)

def softplus_derivative(x):
    return 1 / (1 + np.exp(-x))  # Derivative is the sigmoid function

# Plot the Softplus function and its derivative
def softplus_plot(ax):
    x = np.linspace(-10, 10, 1000)
    y = softplus(x)
    y_derivative = softplus_derivative(x)
    ax.plot(x, y, label="Softplus", color="olive")
    ax.plot(x, y_derivative, label="Derivada de Softplus", color="orange", linestyle="--")
    ax.set_title("Función Softplus")
    ax.set_xlabel("x")
    ax.set_ylabel("Softplus(x)")
    ax.grid(True)
    ax.legend()