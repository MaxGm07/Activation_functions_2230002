import matplotlib.pyplot as plt
from src.identity_function import identity_plot
from src.relu_function import relu_plot
from src.sigmoid_function import sigmoid_plot
from src.step_function import step_plot

fig, axs = plt.subplots(2, 2)
fig.suptitle("Funciones de activación")

sigmoid_plot(axs[0, 0])  
relu_plot(axs[0, 1])
step_plot(axs[1, 0])
identity_plot(axs[1, 1])

plt.tight_layout()
plt.show()
