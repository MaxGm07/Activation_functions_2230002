import numpy as np
import matplotlib.pyplot as plt

# Define the ReLU function and its derivative
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Create a range of values for x
x = np.linspace(-10, 10, 1000)

# Apply the ReLU function and its derivative
y = relu(x)
y_derivative = relu_derivative(x)

# Plot the ReLU function and its derivative
def relu_plot(ax):
    ax.plot(x, y, label="ReLU", color="red")
    ax.plot(x, y_derivative, label="Derivada de ReLU", color="orange", linestyle="--")
    ax.set_title("Función de Activación ReLU")
    ax.set_xlabel("x")
    ax.set_ylabel("ReLU(x)")
    ax.grid(True)
    ax.legend()
