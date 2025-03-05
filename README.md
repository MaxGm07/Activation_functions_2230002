# Activation_functions_2230002

![Badge](https://img.shields.io/badge/Estado-Completado-brightgreen)

:octocat:

Este repositorio contiene la **Tarea 1** del curso de **Visión artificial**. El proyecto está diseñado para graficar las funciones de activación más empleadas dentro del tema de redes neuronales, permitiendo comprender y visualizar en este repositorio las gráficas de dichas funciones con su respectiva derivada.


## Tabla de Contenidos

1. [Descripción](#descripción)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Nota para el entorno virtual](#nota-para-el-entorno-virtual)
5. [Uso](#uso)

---

## Descripción

Este proyecto es parte de la **Tarea 1** del curso de **Visión artificial**. Su objetivo principal es graficar ocho funciones de activacion, siendo la función gaussiana, identidad, reLU, sigmoide, signum, softmax, step (o escalón) y tangente hiperbólica. Aquí se incluyen los archivos de código fuente, documentación y pruebas necesarias para cumplir con los requisitos de la tarea.

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
## Instalación

Sigue estos pasos para clonar y configurar el proyecto en tu máquina local:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/MaxGm07/Tarea_1_2230002.git
2. Navegue mediante el comando cd hasta la carpeta donde clonó el repositorio
3. Cree un nuevo entorno virtual (se describe mejor el procedimiento en el apartado de Nota)
4. Instale la lista de requirements (recomendado: dentro del entorno virtual):
    pip install -r requirements.txt (en unix solo cambia el pip con pip3)



## Nota para el entorno virtual
Se recomienda tener el entorno virtual generado en la carpeta principal para un fácil acceso, su activación y desactivación se realiza de la siguiente forma: 

**En PowerShell:**
    
    .\nombre_del_entorno\Scripts\Activate
    deactivate
    

**En Unix:**

    source nombre_del_entorno/bin/activate
    deactivate
    

## Uso
Finalmente, para emplear este repositorio, con sus respectivos requerimientos y entorno virtual cumplidos, se puede proceder a usar el código *main.py* mediante python main.py en PowerShell y python3 main.py en Linux, mediante la ejecución del código principal, se manda a llamar cada uno de los códigos requeridos para la graficación de las 8 funciones de activación mostrando de igual forma sus respectivas derivadas.

