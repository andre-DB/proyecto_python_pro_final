from ultralytics import YOLO
import os

# Cargar el modelo entrenado
model = YOLO(r"C:\Users\User\Desktop\PROYECTOFINAL\GARBAGE CLASSIFICATION\runs\detect\train\weights\best.pt")

carpeta = r"GARBAGE CLASSIFICATION\videos"

for archivo in os.listdir(carpeta):
    if archivo.endswith((".mp4", ".avi", ".mov", ".mkv")):
        ruta = os.path.join(carpeta, archivo)

        print(f"Procesando {archivo}")

        model.predict(
            source=ruta,
            save=True,
            show=True,
            conf=0.5
        )

print("Proceso terminado.")