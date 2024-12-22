from PIL import Image, ImageDraw, ImageFont
import io
import boto3
import os

# Crear cliente de traducción de AWS
aws_access_key_id = os.getenv('ACCESS_KEY_ID')  # Credenciales desde el .env
aws_secret_access_key = os.getenv('ACCESS_SECRET_KEY')

translate_client = boto3.client(
    service_name='translate',
    region_name='eu-west-2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

#Censura las áreas de texto detectadas en la imagen.
def delete_text(buffer, response):
    img = Image.open(io.BytesIO(buffer))
    draw = ImageDraw.Draw(img)

    margin = 2  # Margen adicional para censura
    censured_area = []

    for detection in response.get('TextDetections', []):
        bounding_box = detection['Geometry']['BoundingBox']
        x = int(img.width * bounding_box['Left'])
        y = int(img.height * bounding_box['Top'])
        w = int(img.width * bounding_box['Width'])
        h = int(img.height * bounding_box['Height'])

        # Aplicar márgenes
        x = max(x - margin, 0)
        y = max(y - margin, 0)
        w = min(w + 2 * margin, img.width - x)
        h = min(h + 2 * margin, img.height - y)

        # Dibujar un rectángulo blanco para censurar
        draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
        censured_area.append((x, y, w, h))

    # Guardar la imagen censurada en memoria
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='JPEG')
    img_byte_array.seek(0)
    return img_byte_array.read(), censured_area

#Traduce texto usando AWS Translate.
def translate_text_with_aws(text, target_lang='es'):
    try:
        result = translate_client.translate_text(Text=text, SourceLanguageCode='en', TargetLanguageCode=target_lang)
        return result['TranslatedText']
    except Exception as e:
        print(f"Error al traducir el texto: {e}")
        return text

# Obtener una fuente que soporte caracteres especiales
def get_font_that_fits(draw, text, max_width, max_height):
    font_size = 10
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Usa Arial para soporte UTF-8
    except IOError:
        print("No se encontró Arial, usando fuente predeterminada.")
        font = ImageFont.load_default()

    while font_size > 1:
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        if text_width <= max_width and text_height <= max_height:
            break

        font_size -= 1
        font = ImageFont.truetype("arial.ttf", font_size)

    return font

def filter_overlapping_detections(text_detections):
    filtered_detections = []
    final_detections = []

    # Convertir las detecciones en una lista de áreas con coordenadas y texto
    for detection in text_detections:
        box = detection['Geometry']['BoundingBox']
        detected_text = detection['DetectedText']
        x = box['Left']
        y = box['Top']
        w = box['Width']
        h = box['Height']
        area = w * h
        filtered_detections.append({
            "DetectedText": detected_text,
            "Area": area,
            "BoundingBox": (x, y, w, h),
            "Confidence": detection['Confidence']
        })

    # Ordenar por área y longitud del texto (priorizamos textos largos y áreas grandes)
    filtered_detections = sorted(filtered_detections, key=lambda x: (-len(x["DetectedText"]), -x["Area"]))

    # Filtrar superposiciones y redundancias
    for current in filtered_detections:
        keep = True
        cx, cy, cw, ch = current["BoundingBox"]
        current_text = current["DetectedText"]

        for other in final_detections:
            ox, oy, ow, oh = other["BoundingBox"]
            other_text = other["DetectedText"]

            # Verificar si hay superposición en el bounding box
            if not (cx + cw < ox or cx > ox + ow or cy + ch < oy or cy > oy + oh):
                # Si el texto actual está contenido en otro texto, descartar
                if current_text in other_text:
                    keep = False
                    break
                # Si el texto más largo ya incluye las palabras actuales, descartar
                if set(current_text.split()).issubset(set(other_text.split())):
                    keep = False
                    break

        if keep:
            final_detections.append(current)

    # Convertir de vuelta al formato esperado
    return [
        {
            "DetectedText": detection["DetectedText"],
            "Geometry": {"BoundingBox": {
                "Left": detection["BoundingBox"][0],
                "Top": detection["BoundingBox"][1],
                "Width": detection["BoundingBox"][2],
                "Height": detection["BoundingBox"][3],
            }},
            "Confidence": detection["Confidence"]
        }
        for detection in final_detections
    ]

def translate_and_reinsert_text(deleted_image, response, target_lang='es'):
    # Filtrar textos redundantes
    clean_detections = filter_overlapping_detections(response.get('TextDetections', []))

    # Resto del flujo igual que antes, trabajando con clean_detections
    img = Image.open(io.BytesIO(deleted_image))
    draw = ImageDraw.Draw(img)

    for detection in clean_detections:
        detected_text = detection['DetectedText']
        translated_text = translate_text_with_aws(detected_text, target_lang)

        # Extraer la posición del bounding box
        bounding_box = detection['Geometry']['BoundingBox']
        x = int(img.width * bounding_box['Left'])
        y = int(img.height * bounding_box['Top'])
        w = int(img.width * bounding_box['Width'])
        h = int(img.height * bounding_box['Height'])

        # Obtener una fuente ajustada
        font = get_font_that_fits(draw, translated_text, w, h)

        # Obtener las dimensiones del texto con la fuente ajustada
        text_bbox = draw.textbbox((0, 0), translated_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Comprobar que el texto no excede el área del bounding box
        if text_width > w:
            print(f"¡Advertencia! El texto '{translated_text}' es demasiado largo para el área asignada.")
            text_width = w  # Ajustar para que no se salga del área

        if text_height > h:
            print(f"¡Advertencia! El texto '{translated_text}' excede la altura del área asignada.")
            text_height = h  # Ajustar para que no se salga del área

        # Centramos el texto
        text_x = x + (w - text_width) / 2
        text_y = y + (h - text_height) / 2

        # Escribir el texto
        draw.text((text_x, text_y), translated_text, font=font, fill=(0, 0, 0))

        # Depuración: imprimir las coordenadas y el tamaño del texto
        #print(f"Texto: '{translated_text}' en ({text_x}, {text_y}), tamaño: {text_width}x{text_height}")

    # Guardar la imagen resultante
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='JPEG')
    img_byte_array.seek(0)
    return img_byte_array.read()

#Borra, traduce y reinserta texto detectado en una imagen.
def translate_text_image(buffer, response, target_lang='es'):
    deleted_image, _ = delete_text(buffer, response)
    translated_image = translate_and_reinsert_text(deleted_image, response, target_lang)
    return translated_image
