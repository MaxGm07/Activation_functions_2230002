# Activation_functions_2230002

![Badge](https://img.shields.io/badge/Estado-Completado-brightgreen)

:octocat:

**Alumno:** Carlos Maximiliano García mediante
**Matrícula:** 2230002
**Asignatura:** Visión artificial

Este repositorio contiene la **Tarea 1** del curso de **Visión artificial**. El proyecto está diseñado para graficar las funciones de activación más empleadas dentro del tema de redes neuronales, permitiendo comprender y visualizar en este repositorio las gráficas de dichas funciones con su respectiva derivada.


## Tabla de Contenidos

1. [Descripción](#descripción)
2. [¿Qué son las funcones de activacion?](#qué-son-las-funciones-de-activación)
3. [Requisitos](#requisitos)
5. [Nota para el entorno virtual](#nota-para-el-entorno-virtual)

6. [Uso](#uso)
7. [Funciones](#funciones)
8. [Instalación](#instalación)
---

## Descripción

Este proyecto es parte de la **Tarea 1** del curso de **Visión artificial**. Su objetivo principal es graficar ocho funciones de activacion, siendo la función gaussiana, identidad, reLU, sigmoide, signum, softmax, step (o escalón) y tangente hiperbólica. Aquí se incluyen los archivos de código fuente, documentación y pruebas necesarias para cumplir con los requisitos de la tarea.

---
## ¿Qué son las funciones de activación?
Las funciones de activación, en redes neuronales son funciones matemáticas que se aplican a la salida de cada neurona para determinar si debe activarse (enviar información a la siguiente capa) o no. Estas funciones introducen no linealidades en el modelo, lo que permite que la red aprenda y represente relaciones complejas en los datos.

---
## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- [Python 3.8 o superior](https://www.python.org/downloads/) 

Un punto importante es la creación de un entorno virtual para probar el código principal mediante el comando

**en PowerShell**
    
    python -m venv nombre_del_entorno 

**en Unix**

    python3 -m venv nombre_del_entorno  

además de contar con las librerías requeridas listadas en el archivo requirements.txt
su instalación se facilita mediante el comando mostrado en el apartado de instalación, para Windows (Powershell) y Linux


---


## Nota para el entorno virtual
Se recomienda tener el entorno virtual generado en la carpeta principal para un fácil acceso, su activación y desactivación se realiza de la siguiente forma: 

**En PowerShell:**
    
    .\nombre_del_entorno\Scripts\Activate
    deactivate
    

**En Unix:**

    source nombre_del_entorno/bin/activate
    deactivate
---   
## Estructura del proyecto
```
Activation_functions_2230002/
├── src/
│   ├── gaussian_function.py
│   ├── identity_function.py
│   ├── relu_function.py
│   ├── sigmoid_function.py
│   ├── signum_function.py
│   ├── softplus_function.py
│   ├── step_function.py
│   ├── tanh_function.py
├── .gitignore
├── README.md
├── main.py
└── requirements.txt
```

## Uso
Finalmente, para emplear este repositorio, con sus respectivos requerimientos y entorno virtual cumplidos, se puede proceder a usar el código *main.py* mediante python main.py en PowerShell y python3 main.py en Linux, mediante la ejecución del código principal, se manda a llamar cada uno de los códigos requeridos para la graficación de las 8 funciones de activación mostrando de igual forma sus respectivas derivadas.
---
## Funciones

En el presente proyecto se grafican las siguientes funciones de activacion:

1. Función Gaussiana (Gaussian Function):
   - Función: exp(-x^2)
   - Derivada: -2 * x * exp(-x^2)

2. Función Identidad (Identity Function):
   - Función: Devuelve el mismo valor de entrada.
   - Derivada: 1 para todos los valores de x.

3. Función ReLU (Rectified Linear Unit):
   - Función: Devuelve 0 si x < 0; de lo contrario, devuelve x.
   - Derivada: 0 si x < 0; 1 si x >= 0.

4. Función Sigmoide (Sigmoid Function):
   - Función: Mapea cualquier valor a un rango entre 0 y 1.
   - Derivada: sigmoide(x) * (1 - sigmoide(x)).

5. Función Signo (Signum Function):
   - Función: Devuelve -1 si x < 0, 0 si x = 0, y 1 si x > 0.
   - Derivada: No está definida en x = 0; en otros puntos, es 0.

6. Función Softplus (Softplus Function):
   - Función: log(1 + exp(x)).
   - Derivada: 1 / (1 + exp(-x)).

7. Función Escalón (Step Function):
   - Función: Devuelve 1 si x >= 0; de lo contrario, devuelve 0.
   - Derivada: No está definida en x = 0; en otros puntos, es 0.

8. Función Tangente Hiperbólica (TanH):
   - Función: Mapea cualquier valor a un rango entre -1 y 1.
   - Derivada: 1 - tanh(x)^2.


## Instalación

Sigue estos pasos para clonar y configurar el proyecto en tu máquina local:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/MaxGm07/Tarea_1_2230002.git
2. Navegue mediante el comando cd hasta la carpeta donde clonó el repositorio
3. Cree un nuevo entorno virtual (se describe mejor el procedimiento en el apartado de Nota)
4. Instale la lista de requirements (recomendado: dentro del entorno virtual):
    pip install -r requirements.txt (en unix solo cambia el pip con pip3)
