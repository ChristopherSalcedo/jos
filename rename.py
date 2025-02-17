import os

# 📌 Ruta de la carpeta (MODIFICA SEGÚN TU CASO)
carpeta_imagenes = r"C:\Users\chsg6\Downloads\New folder\imagenes"

def renombrar_imagenes(carpeta):
    if not os.path.exists(carpeta):
        print(f"❌ La carpeta '{carpeta}' no existe. Verifica la ruta.")
        return
    
    # 📌 Filtra solo imágenes (evita renombrar videos u otros archivos)
    imagenes = sorted(
        [f for f in os.listdir(carpeta) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    )

    if not imagenes:
        print("⚠️ No se encontraron imágenes en la carpeta.")
        return

    # 📌 Paso 1: Renombrar temporalmente para evitar conflictos
    temp_names = []
    for i, imagen in enumerate(imagenes):
        extension = os.path.splitext(imagen)[1]  # Obtiene la extensión (.jpg, .png, etc.)
        nombre_temp = os.path.join(carpeta, f"temp_{i}{extension}")
        os.rename(os.path.join(carpeta, imagen), nombre_temp)
        temp_names.append(nombre_temp)  # Guarda los nombres temporales

    # 📌 Paso 2: Renombrar con el formato imagenX.jpg
    for i, temp_file in enumerate(sorted(temp_names)):
        extension = os.path.splitext(temp_file)[1]  # Mantiene la extensión original
        nuevo_nombre = os.path.join(carpeta, f"imagen{i+1}{extension}")
        os.rename(temp_file, nuevo_nombre)

    print(f"✅ Renombradas {len(imagenes)} imágenes correctamente en '{carpeta}'.")

renombrar_imagenes(carpeta_imagenes)
