#!/usr/bin/python3

import os
import boto3
from flask import Flask, request, Response, abort
from dotenv import load_dotenv
from detect_text import detect_text
from translate_text import translate_text_image

# Cargar variables de entorno de .env
load_dotenv()

# Guardar variables de entorno
accessKeyId = os.environ.get('ACCESS_KEY_ID')
secretKey = os.environ.get('ACCESS_SECRET_KEY')
bucket_name = os.environ.get('BUCKET')
region = os.environ.get('REGION')
input_folder = "input"
output_folder = "output"

# Crear servidor Flask
application = Flask(__name__)

# Crear el servicio S3 y darle las credenciales
s3 = boto3.Session(
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretKey,
    region_name=region
).resource('s3')

# api/analyze endpoint
@application.route('/api/analyze', methods=['POST'])
def analyzeImage():
    # Obtener el nombre de la imagen del método POST
    key = request.get_json()['key']
    if key is None:
        abort(400)
    
    try:
        # Construir la ruta completa de la imagen dentro de la carpeta "input"
        input_key = f"{input_folder}/{key}"
        # Construir la ruta para la imagen traducida en la carpeta "output"
        output_key = f"{output_folder}/result_{key}"

        # Detectar texto en la imagen
        response = detect_text(input_key)

        # Descargar la imagen de la carpeta "input"
        fileObject = s3.Object(bucket_name, input_key).get()
        fileContent = fileObject['Body'].read()

        # Traducir el texto y reemplazarlo en la imagen
        translated_image = translate_text_image(fileContent, response, 'es')

        # Subir la nueva imagen traducida al bucket (en la carpeta "output")
        s3.Object(bucket_name, output_key).put(Body=translated_image)
    except Exception as error:
        print(error)
        abort(500)
    return Response(status=200)

# Ejecutar el servidor Flask
if __name__ == "__main__":
    application.debug = True
    application.run()  # http://127.0.0.1:5000/
