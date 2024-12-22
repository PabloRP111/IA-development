# 🌟 Proyecto AWS

Este proyecto utiliza los servicios de Amazon Web Services (AWS). Sigue estas instrucciones para configurarlo y probarlo correctamente.

---

## 📄 Subject

El tema del proyecto está descrito en detalle en el siguiente documento:

📄 [Ver documentación](./Proyecto_AWS.pdf)

---

## 🛠️ Requisitos Previos

Para probar este proyecto necesitarás tener:

1. Una **cuenta de AWS** activa.
2. Un **bucket en AWS** configurado.
3. **Claves de acceso a AWS**:
   - Clave pública.
   - Clave privada.

---

## 🚀 Cómo Configurar

1. **Crea un bucket en AWS S3** si no tienes uno configurado:
   - Accede a la consola de AWS.
   - Ve a la sección de S3 y crea un bucket.

2. **Genera tus claves de acceso**:
   - Ve a la consola de AWS.
   - Dirígete a "IAM" > "Users" y selecciona tu usuario.
   - Crea un nuevo par de claves de acceso (pública y privada).

3. **Configura las claves en tu entorno**:
   - Añade las claves en las variables de entorno, por ejemplo:
     ```cmd
     export AWS_ACCESS_KEY_ID=tu_clave_publica
     export AWS_SECRET_ACCESS_KEY=tu_clave_privada
     ```

---

## ⚙️ Ejecución

1. Clona este repositorio:
   ```cmd
   git clone https://github.com/PabloRP111/IA-development/tree/main/aws-proyect
   cd al repositorio
   ```

2. Instala las dependencias necesarias (requirements):
   ```cmd
   pip install -r requirements.txt
   ```

3. Ejecuta el proyecto:
   ```cmd
   python nombre-del-ejecutable.py
   ```

---

## 🤝 Créditos

Este proyecto utiliza servicios de AWS para demostrar el uso de buckets y autenticación mediante claves de acceso.
