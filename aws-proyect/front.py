#!/usr/bin/python3

import os
import requests
from tkinter import Tk, Label, Button, Canvas, Frame, filedialog, messagebox
from PIL import Image, ImageTk
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_URL = "http://127.0.0.1:5000/api/analyze"  # URL del servidor Flask
BUCKET_NAME = os.getenv('BUCKET')
region = os.environ.get('REGION')

# Variables globales
selected_image_path = None
result_image = None
input_folder = "input"
output_folder = "output"

# Función para seleccionar una imagen
def seleccionar_imagen():
    global selected_image_path
    filepath = filedialog.askopenfilename(
        filetypes=[("Archivos JPG", "*.jpg")],
        title="Selecciona una imagen JPG"
    )
    if filepath:
        selected_image_path = filepath
        cargar_imagen_en_canvas(filepath)

# Función para mostrar la imagen seleccionada en el canvas
def cargar_imagen_en_canvas(filepath):
    global result_image
    image = Image.open(filepath)
    image.thumbnail((300, 300))
    result_image = ImageTk.PhotoImage(image)
    canvas.delete("all")
    canvas.create_image(150, 150, image=result_image)

# Función para subir la imagen a S3
def subir_imagen_a_s3():
    global selected_image_path
    if not selected_image_path:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una imagen primero.")
        return None

    try:
        # Nombre de la imagen en el bucket S3
        image_key = os.path.basename(selected_image_path)
        input_key = f"{input_folder}/{image_key}"

        # Subir archivo al bucket
        with open(selected_image_path, "rb") as file:
            response = requests.put(
                f"https://{BUCKET_NAME}.s3.{region}.amazonaws.com/{input_key}",
                data=file
            )
            if response.status_code == 200:
                return image_key  # Retornar el nombre del archivo subido
            else:
                messagebox.showerror("Error", f"Error al subir la imagen: {response.text}")
                return None
    except Exception as e:
        messagebox.showerror("Error", f"Error al subir la imagen: {e}")
        return None

# Función para procesar la imagen
def procesar_imagen():
    image_key = subir_imagen_a_s3()
    if not image_key:
        return

    try:
        # Llamar al endpoint de Flask para analizar la imagen
        response = requests.post(
            API_URL,
            json={"key": image_key}
        )
        if response.status_code == 200:
            descargar_imagen_procesada(image_key)
        else:
            messagebox.showerror("Error", f"Error al procesar la imagen: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al procesar la imagen: {e}")

# Función para descargar la imagen procesada desde S3
def descargar_imagen_procesada(image_key):
    try:
        # Ruta de la imagen procesada
        output_key = f"{output_folder}/result_{image_key}"
        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{output_key}"

        # Descargar la imagen procesada
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filepath = f"./imgs/procesada_{os.path.basename(image_key)}"
            with open(filepath, "wb") as file:
                file.write(response.content)

            cargar_imagen_en_canvas(filepath)
            messagebox.showinfo("Procesado", "La imagen ha sido procesada y descargada con éxito.")
        else:
            messagebox.showerror("Error", f"Error al descargar la imagen procesada: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al descargar la imagen procesada: {e}")

# Configurar la ventana principal
root = Tk()
root.title("Traductor de Imágenes con AWS")
root.configure(bg="#f7f7f7")

# Crear marcos para organización
frame_top = Frame(root, bg="#f7f7f7")
frame_top.pack(pady=20)

frame_canvas = Frame(root, bg="#f7f7f7")
frame_canvas.pack(pady=10)

frame_buttons = Frame(root, bg="#f7f7f7")
frame_buttons.pack(pady=20)

# Etiqueta para instrucciones
Label(frame_top, text="Traductor de Imágenes con AWS", font=("Arial", 16, "bold"), bg="#f7f7f7").pack()
Label(frame_top, text="Selecciona una imagen JPG para procesar", font=("Arial", 12), bg="#f7f7f7").pack()

# Canvas para mostrar la imagen seleccionada
canvas = Canvas(frame_canvas, width=300, height=300, bg="#d9d9d9", relief="ridge", bd=2)
canvas.pack()

# Botones
Button(frame_buttons, text="Seleccionar Imagen", command=seleccionar_imagen, bg="#4CAF50", fg="white", font=("Arial", 10)).pack(side="left", padx=10)
Button(frame_buttons, text="Procesar Imagen", command=procesar_imagen, bg="#2196F3", fg="white", font=("Arial", 10)).pack(side="left", padx=10)

# Configuración de la ventana
ancho_ventana = 500
alto_ventana = 550
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# Centrar imagen
pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)

root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
root.iconbitmap("./imgs/aws.ico") #Icono
root.mainloop()
