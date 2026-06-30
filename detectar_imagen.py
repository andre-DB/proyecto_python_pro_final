from ultralytics import YOLO

# Cargar el modelo entrenado
model = YOLO(r"C:\Users\User\Desktop\PROYECTOFINAL\GARBAGE CLASSIFICATION\runs\detect\train\weights\best.pt")

# Analizar una imagen
results = model.predict(
    source=r"C:\Users\User\Desktop\PROYECTOFINAL\GARBAGE CLASSIFICATION\imagenes\imagen2.png",  # Cambia por el nombre de tu imagen
    save=True,
    show=True,
    conf=0.5
)

print("Imagen analizada.")
print("Guardada en:", results[0].save_dir)