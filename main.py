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
    # Crear una figura con una cuadrícula de 2x4
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))
    fig.suptitle("Funciones de Activación y sus Derivadas", fontsize=16, y=0.99) #Título y ajuste del título y escrito

    # Graficar cada función en su respectivo subplot
    sigmoid_plot(axs[0, 0])  # Sigmoid en la posición (0, 0)
    relu_plot(axs[0, 1])     # ReLU en la posición (0, 1)
    step_plot(axs[1, 0])     # Escalón en la posición (1, 0)
    identity_plot(axs[1, 1]) # Identidad en la posición (1, 1)
    gaussian_plot(axs[0, 2]) # Gaussiana en la posición (0, 2)
    tanh_plot(axs[1, 2])     # Tangente Hiperbólica en la posición (1, 2)
    signum_plot(axs[0, 3])   # Signum en la posición (0, 3)
    softplus_plot(axs[1, 3]) # Softplus en la posición (1, 3)

    # Ajustar el layout para evitar superposiciones
    plt.tight_layout()

    # Ajustar el espacio entre los subplots
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1, wspace=0.3, hspace=0.3)


    # Mostrar la figura
    plt.show()

if __name__=="__main__":
    main_plot()