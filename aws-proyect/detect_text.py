import os
import boto3
from dotenv import load_dotenv

# Cargar las variables de entorno .env
load_dotenv()

# Guardar las variables de entorno
accessKeyId = os.environ.get('ACCESS_KEY_ID')
secretKey = os.environ.get('ACCESS_SECRET_KEY')
bucket = os.environ.get('BUCKET')
region = os.environ.get('REGION')

# Crear el servicio de Rekognition
rekognition_client = boto3.Session(
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretKey,
    region_name=region).client('rekognition')

# Función que detecta texto
def detect_text(img):
    try:
        response = rekognition_client.detect_text(
            Image={'S3Object': {'Bucket': bucket, 'Name': img}}
        )

        print("Detección de texto completada correctamente ;)")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

    return response
