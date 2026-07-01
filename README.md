# ♻️ Detector Inteligente de Residuos con YOLOv8

Autor: Richard André

## Descripción:

Este proyecto consiste en desarrollar un sistema de visión por computadora utilizando Python y YOLOv8 para detectar y clasificar distintos tipos de residuos reciclables en imágenes y videos. El sistema identifica automáticamente materiales como plástico, papel, cartón, vidrio, metal y residuos biodegradables, mostrando su ubicación mediante cuadros y etiquetas.

## 📌 Finalidad del proyecto:

El objetivo de este proyecto es desarrollar un sistema inteligente capaz de detectar y clasificar diferentes tipos de residuos reciclables mediante técnicas de visión por computadora e inteligencia artificial. Para ello, se entrenó un modelo YOLOv8 con un conjunto de imágenes clasificadas en seis categorías: plástico, papel, cartón, vidrio, metal y residuos biodegradables.

El sistema permite analizar imágenes y videos, identificando automáticamente los residuos presentes y mostrando su ubicación mediante cuadros delimitadores y etiquetas. Esto facilita el reconocimiento de los materiales de forma rápida y precisa.

Este proyecto puede utilizarse como una herramienta de apoyo para fomentar el reciclaje, servir como demostración educativa del uso de la inteligencia artificial en el cuidado del medio ambiente, y como base para futuros desarrollos, como contenedores inteligentes, sistemas automáticos de clasificación de residuos o aplicaciones de monitoreo ambiental.

## ⚙️ Funciones y características

### 🔍 Detección automática de residuos
El sistema utiliza un modelo de inteligencia artificial basado en YOLOv8 para detectar automáticamente diferentes tipos de residuos presentes en imágenes y videos.

### 🗂️ Clasificación de residuos
El modelo identifica los siguientes tipos de materiales:
- 🌱 Biodegradable
- 📦 Cartón
- 🍾 Vidrio
- 🥫 Metal
- 📄 Papel
- ♻️ Plástico

### 🖼️ Análisis de imágenes
Permite analizar imágenes individuales y detectar los residuos presentes, mostrando un recuadro sobre cada objeto identificado junto con el nombre de la categoría correspondiente.

### 🎥 Análisis de videos
Procesa videos completos cuadro por cuadro, detectando los residuos durante toda la reproducción y generando un nuevo video con las detecciones realizadas.

### 🧠 Modelo entrenado con YOLOv8
El proyecto utiliza un modelo personalizado entrenado con un conjunto de datos de residuos reciclables, lo que permite obtener mejores resultados para este tipo de objetos.

### 💾 Guardado automático de resultados
Las imágenes y videos procesados se guardan automáticamente en la carpeta de resultados (`runs/detect/predict`), facilitando su revisión posterior.

### ⚡ Desarrollo en Python
El sistema fue desarrollado en Python utilizando bibliotecas especializadas como Ultralytics YOLOv8, OpenCV y PyTorch, lo que permite un procesamiento eficiente y la posibilidad de ampliar el proyecto en el futuro.

## 🚀 Instalación y uso del proyecto

### Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

- Python 3.10 o superior.
- Git (opcional, para clonar el repositorio).

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
```

### 2. Ingresar a la carpeta del proyecto

```bash
cd GARBAGE-CLASSIFICATION
```

### 3. Instalar las dependencias

Instala las bibliotecas necesarias con el siguiente comando:

```bash
pip install ultralytics opencv-python
```

### 4. Ejecutar el proyecto

#### Entrenar el modelo

```bash
python detector.py
```

#### Analizar una imagen

```bash
python detectar_imagen.py
```

#### Analizar un video

```bash
python detectar_videos.py
```

### Resultados

Las imágenes y videos procesados se guardarán automáticamente en la carpeta:

```
runs/detect/predict
```

donde podrán visualizarse los residuos detectados con sus respectivas etiquetas y cuadros delimitadores.

## 💬 Comentarios

Este proyecto se encuentra en constante mejora, por lo que cualquier sugerencia o aporte será bien recibido.

Si encuentras algún error, tienes una idea para mejorar el sistema o deseas agregar nuevas funcionalidades, puedes crear un **Issue** en este repositorio o enviar un **Pull Request** con tus cambios.

Algunas mejoras que podrían implementarse en el futuro son:

- Detección en tiempo real mediante cámara web.
- Mayor precisión en la clasificación de residuos.
- Desarrollo de una interfaz gráfica más intuitiva.
- Generación de reportes automáticos con estadísticas de los residuos detectados.
- Integración con contenedores inteligentes para automatizar el proceso de reciclaje.

---

## ✅ Conclusión

El desarrollo de este proyecto demuestra cómo la inteligencia artificial y la visión por computadora pueden utilizarse para resolver problemas relacionados con el cuidado del medio ambiente. Mediante el uso de YOLOv8 fue posible entrenar un modelo capaz de detectar y clasificar diferentes tipos de residuos en imágenes y videos de forma automática.

Este sistema puede servir como herramienta educativa, apoyo para proyectos de reciclaje y base para futuras aplicaciones inteligentes orientadas a mejorar la gestión de residuos. Además, el proyecto demuestra el potencial de las tecnologías de aprendizaje profundo para desarrollar soluciones innovadoras que contribuyan a una sociedad más responsable con el medio ambiente.
