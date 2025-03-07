import numpy as np
import matplotlib.pyplot as plt

# Define the Hyperbolic Tangent function and its derivative
def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x)**2

# Create a range of values for x
x = np.linspace(-10, 10, 1000)

# Apply the Hyperbolic Tangent function and its derivative
y = tanh(x)
y_derivative = tanh_derivative(x)

# Plot the Hyperbolic Tangent function and its derivative
def tanh_plot(ax):
    ax.plot(x, y, label="Tangente Hiperbólica", color="salmon")
    ax.plot(x, y_derivative, label="Derivada de Tangente Hiperbólica", color="orange", linestyle="--")
    ax.set_title("Función Tangente Hiperbólica")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()