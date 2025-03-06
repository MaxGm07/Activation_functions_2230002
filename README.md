# Activation Functions 2230002

![Estado](https://img.shields.io/badge/Estado-Completado-brightgreen)

:octocat:

**Alumno:** Carlos Maximiliano García Medina  
**Matrícula:** 2230002  
**Asignatura:** Visión Artificial  

Este repositorio contiene la **Tarea 1** del curso de **Visión Artificial**. Su propósito es graficar las funciones de activación más utilizadas en redes neuronales, junto con sus respectivas derivadas, para facilitar su comprensión y análisis.

---
## 📖 Tabla de Contenidos
1. [Descripción](#descripción)
2. [¿Qué son las funciones de activación?](#qué-son-las-funciones-de-activación)
3. [Requisitos](#requisitos)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Funciones](#funciones)
6. [Instalación](#instalación)
7. [Uso](#uso)
8. [Entorno Virtual](#entorno-virtual)

---
## 📌 Descripción
Este proyecto es parte de la **Tarea 1** del curso de **Visión Artificial**. Su objetivo principal es graficar ocho funciones de activación ampliamente utilizadas en redes neuronales:

- Gaussiana
- Identidad
- ReLU
- Sigmoide
- Signum
- Softplus
- Escalón (Step)
- Tangente Hiperbólica

El repositorio incluye los archivos de código fuente, documentación y pruebas necesarias para cumplir con los requisitos de la tarea.

---
## 🤖 ¿Qué son las funciones de activación?
Las funciones de activación en redes neuronales son funciones matemáticas que determinan si una neurona debe activarse o no. Introducen no linealidad en el modelo, permitiendo que la red aprenda y represente relaciones complejas en los datos.

---
## 🔧 Requisitos
Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- [Python 3.8 o superior](https://www.python.org/downloads/)

---
## 📂 Estructura del Proyecto
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

---
## 📊 Funciones
El proyecto grafica las siguientes funciones de activación junto con sus derivadas:

1. **Gaussiana**: exp(-x²)  
   - Derivada: -2x * exp(-x²)

2. **Identidad**: f(x) = x  
   - Derivada: 1

3. **ReLU (Rectified Linear Unit)**: f(x) = max(0, x)  
   - Derivada: 0 si x < 0; 1 si x >= 0

4. **Sigmoide**: 1 / (1 + exp(-x))  
   - Derivada: sigmoide(x) * (1 - sigmoide(x))

5. **Signum**:
   - f(x) = -1 si x < 0, 0 si x = 0, 1 si x > 0
   - Derivada: No definida en x = 0; en otros puntos es 0

6. **Softplus**: log(1 + exp(x))  
   - Derivada: 1 / (1 + exp(-x))

7. **Escalón (Step)**:
   - f(x) = 1 si x >= 0; de lo contrario, 0
   - Derivada: No definida en x = 0; en otros puntos es 0

8. **Tangente Hiperbólica (TanH)**: tanh(x)  
   - Derivada: 1 - tanh²(x)

---
## ⚙️ Instalación
Para clonar y configurar el proyecto en tu máquina local, sigue estos pasos:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/MaxGm07/Tarea_1_2230002.git
   ```
2. Navega hasta la carpeta del repositorio:
   ```bash
   cd Tarea_1_2230002
   ```
3. Crea un entorno virtual (ver sección [Entorno Virtual](#entorno-virtual))
4. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```
   *(En Unix, usa `pip3` en lugar de `pip` si es necesario.)*

---
## 🚀 Uso
Una vez que el entorno virtual y los requisitos estén configurados, puedes ejecutar el código principal con:

```bash
python main.py  # En Windows
python3 main.py # En Linux/macOS
```

Esto generará las gráficas de las ocho funciones de activación junto con sus derivadas.

---
## 🛠️ Entorno Virtual
Se recomienda crear un entorno virtual para evitar conflictos con dependencias de otros proyectos. Sigue estos pasos:

### 🔹 Creación del entorno virtual

**En Windows (PowerShell):**
```powershell
python -m venv nombre_del_entorno
```

**En Unix (Linux/macOS):**
```bash
python3 -m venv nombre_del_entorno
```

### 🔹 Activación del entorno virtual

**En Windows (PowerShell):**
```powershell
.
ombre_del_entorno\Scripts\Activate
```

**En Unix (Linux/macOS):**
```bash
source nombre_del_entorno/bin/activate
```

### 🔹 Instalación de dependencias
Una vez activado el entorno virtual, instala las dependencias con:
```bash
pip install -r requirements.txt
```

### 🔹 Desactivación del entorno virtual
Para salir del entorno virtual, usa:
```bash
deactivate
```

---
## 📌 Notas
- Se recomienda mantener el entorno virtual en la carpeta principal del proyecto para un acceso más fácil.
- La ejecución de `main.py` generará las gráficas automáticamente sin necesidad de configuración adicional.

---
## 📢 Contacto
Si tienes dudas o sugerencias, no dudes en contactarme a través de GitHub.

¡Gracias por visitar este repositorio! 😊

