import numpy as np
import matplotlib.pyplot as plt

# Define the Sigmoid function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Create a range of values for x
x = np.linspace(-10, 10, 1000)

# Apply the Sigmoid function and its derivative
y = sigmoid(x)
y_derivative = sigmoid_derivative(x)

# Plot the Sigmoid function
def sigmoid_plot(ax):
    ax.plot(x, y, label="Sigmoid", color="red")
    ax.plot(x, y_derivative, label="Derivada de Sigmoid", color="orange", linestyle="--")
    ax.set_title("Función de Activación Sigmoid")
    ax.set_xlabel("x")
    ax.set_ylabel("Sigmoid(x)")
    ax.grid(True)
    ax.legend()

