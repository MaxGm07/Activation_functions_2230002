import numpy as np
import matplotlib.pyplot as plt

# Define the Step function and its derivative
def step(x):
    return np.where(x >= 0, 1, 0)

def step_derivative(x):
    return np.zeros_like(x)  # Derivative is 0 everywhere except at x=0

# Create a range of values for x
x = np.linspace(-10, 10, 1000)

# Apply the Step function and its derivative
y = step(x)
y_derivative = step_derivative(x)

# Plot the Step function and its derivative
def step_plot(ax):
    ax.plot(x, y, label="Escalón", color="magenta")
    ax.plot(x, y_derivative, label="Derivada de escalón", color="orange", linestyle="--")
    ax.set_title("Función de Activación Escalón")
    ax.set_xlabel("x")
    ax.set_ylabel("Step(x)")
    ax.grid(True)
    ax.legend()