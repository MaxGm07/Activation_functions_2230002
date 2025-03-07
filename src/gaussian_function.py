import numpy as np
import matplotlib.pyplot as plt

# Define the Gaussian function and its derivative
def gaussian(x):
    return np.exp(-x**2)

def gaussian_derivative(x):
    return -2 * x * np.exp(-x**2)

# Create a range of values for x
x = np.linspace(-5, 5, 1000)

# Apply the Gaussian function and its derivative
y = gaussian(x)
y_derivative = gaussian_derivative(x)

# Plot the Gaussian function and its derivative
def gaussian_plot(ax):
    ax.plot(x, y, label="Gaussiana", color="blue")
    ax.plot(x, y_derivative, label="Derivada de Gaussiana", color="orange", linestyle="--")
    ax.set_title("Función Gaussiana")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()
