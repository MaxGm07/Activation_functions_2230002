import matplotlib.pyplot as plt
from src.identity_function import identity_plot
from src.relu_function import relu_plot
from src.sigmoid_function import sigmoid_plot
from src.step_function import step_plot
from src.gaussian_function import gaussian_plot
from src.tanh_function import tanh_plot
from src.signum_function import signum_plot
from src.softplus_function import softplus_plot

def main_plot():
    # Create a figure with a 2x4 grid
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))
    fig.suptitle("Funciones de Activación y sus Derivadas", fontsize=16, y=0.99)  # Title and adjustment of the title and text

    # Plot each function in its respective subplot
    sigmoid_plot(axs[0, 0])  # Sigmoid at position (0, 0)
    relu_plot(axs[0, 1])     # ReLU at position (0, 1)
    step_plot(axs[1, 0])     # Step at position (1, 0)
    identity_plot(axs[1, 1]) # Identity at position (1, 1)
    gaussian_plot(axs[0, 2]) # Gaussian at position (0, 2)
    tanh_plot(axs[1, 2])     # Hyperbolic Tangent at position (1, 2)
    signum_plot(axs[0, 3])   # Signum at position (0, 3)
    softplus_plot(axs[1, 3]) # Softplus at position (1, 3)

    # Adjust layout to avoid overlaps
    plt.tight_layout()

    # Adjust the space between subplots
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1, wspace=0.3, hspace=0.3)

    # Display the figure
    plt.show()

if __name__=="__main__":
    main_plot()