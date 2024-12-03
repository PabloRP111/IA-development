import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Cargar el modelo guardado
@st.cache
def cargar_modelo():
    with open('churn-model.pck', 'rb') as file:
        return pickle.load(file)

# Cargar el modelo
modelo_regresion = cargar_modelo()

# Título de la app
st.title("Predicción de Telco - Modelo de Regresión Lineal")

# Explicación de la app
st.write("""
Esta aplicación utiliza un modelo de regresión lineal entrenado sobre el dataset Telco para predecir características relacionadas con clientes de telecomunicaciones.
Introduce los valores de las variables para hacer una predicción.
""")

# Entradas del usuario
st.sidebar.header("Introduce las características del cliente")

# Variables categóricas y numéricas
gender = st.sidebar.selectbox("Género", ['Femenino', 'Masculino'])
seniorcitizen = st.sidebar.selectbox("Senior Citizen (1=Sí, 0=No)", [1, 0])
partner = st.sidebar.selectbox("Tiene pareja", ['Sí', 'No'])
dependents = st.sidebar.selectbox("Tiene dependientes", ['Sí', 'No'])
tenure = st.sidebar.number_input("Años de permanencia", min_value=0, max_value=72, value=12)
phoneservice = st.sidebar.selectbox("Tiene servicio telefónico", ['Sí', 'No'])
multiplelines = st.sidebar.selectbox("Tiene múltiples líneas", ['Sí', 'No', 'No phone service'])
internetservice = st.sidebar.selectbox("Servicio de Internet", ['Fibra óptica', 'DSL', 'No internet service'])
onlinesecurity = st.sidebar.selectbox("Seguridad online", ['Sí', 'No', 'No internet service'])
onlinebackup = st.sidebar.selectbox("Copia de seguridad online", ['Sí', 'No', 'No internet service'])
deviceprotection = st.sidebar.selectbox("Protección de dispositivo", ['Sí', 'No', 'No internet service'])
techsupport = st.sidebar.selectbox("Soporte técnico", ['Sí', 'No', 'No internet service'])
streamingtv = st.sidebar.selectbox("Streaming TV", ['Sí', 'No', 'No internet service'])
streamingmovies = st.sidebar.selectbox("Streaming Movies", ['Sí', 'No', 'No internet service'])
contract = st.sidebar.selectbox("Tipo de contrato", ['Mes a mes', 'Un año', 'Dos años'])
paperlessbilling = st.sidebar.selectbox("Facturación sin papel", ['Sí', 'No'])
paymentmethod = st.sidebar.selectbox("Método de pago", ['Banco', 'Cheque electrónico', 'Transferencia bancaria', 'Crédito automático'])
monthlycharges = st.sidebar.number_input("Cargo mensual", min_value=0, value=70)
totalcharges = st.sidebar.number_input("Cargo total", min_value=0, value=200)

# Preprocesar las variables categóricas
def preprocesar_datos(input_data):
    input_data['gender'] = 1 if input_data['gender'] == 'Masculino' else 0
    input_data['partner'] = 1 if input_data['partner'] == 'Sí' else 0
    input_data['dependents'] = 1 if input_data['dependents'] == 'Sí' else 0
    input_data['phoneservice'] = 1 if input_data['phoneservice'] == 'Sí' else 0
    input_data['multiplelines'] = 1 if input_data['multiplelines'] == 'Sí' else (0 if input_data['multiplelines'] == 'No phone service' else -1)
    input_data['internetservice'] = 0 if input_data['internetservice'] == 'No internet service' else (1 if input_data['internetservice'] == 'DSL' else 2)
    input_data['onlinesecurity'] = 1 if input_data['onlinesecurity'] == 'Sí' else (0 if input_data['onlinesecurity'] == 'No internet service' else -1)
    input_data['onlinebackup'] = 1 if input_data['onlinebackup'] == 'Sí' else (0 if input_data['onlinebackup'] == 'No internet service' else -1)
    input_data['deviceprotection'] = 1 if input_data['deviceprotection'] == 'Sí' else (0 if input_data['deviceprotection'] == 'No internet service' else -1)
    input_data['techsupport'] = 1 if input_data['techsupport'] == 'Sí' else (0 if input_data['techsupport'] == 'No internet service' else -1)
    input_data['streamingtv'] = 1 if input_data['streamingtv'] == 'Sí' else (0 if input_data['streamingtv'] == 'No internet service' else -1)
    input_data['streamingmovies'] = 1 if input_data['streamingmovies'] == 'Sí' else (0 if input_data['streamingmovies'] == 'No internet service' else -1)
    input_data['contract'] = 0 if input_data['contract'] == 'Mes a mes' else (1 if input_data['contract'] == 'Un año' else 2)
    input_data['paperlessbilling'] = 1 if input_data['paperlessbilling'] == 'Sí' else 0
    input_data['paymentmethod'] = 0 if input_data['paymentmethod'] == 'Banco' else (1 if input_data['paymentmethod'] == 'Cheque electrónico' else (2 if input_data['paymentmethod'] == 'Transferencia bancaria' else 3))
    
    return input_data

# Crear un DataFrame con los datos introducidos
nuevos_datos = pd.DataFrame({
    'gender': [gender],
    'seniorcitizen': [seniorcitizen],
    'partner': [partner],
    'dependents': [dependents],
    'tenure': [tenure],
    'phoneservice': [phoneservice],
    'multiplelines': [multiplelines],
    'internetservice': [internetservice],
    'onlinesecurity': [onlinesecurity],
    'onlinebackup': [onlinebackup],
    'deviceprotection': [deviceprotection],
    'techsupport': [techsupport],
    'streamingtv': [streamingtv],
    'streamingmovies': [streamingmovies],
    'contract': [contract],
    'paperlessbilling': [paperlessbilling],
    'paymentmethod': [paymentmethod],
    'monthlycharges': [monthlycharges],
    'totalcharges': [totalcharges]
})

# Preprocesar los datos antes de hacer la predicción
nuevos_datos_procesados = preprocesar_datos(nuevos_datos)

# Realizar la predicción con el modelo cargado
if st.sidebar.button('Predecir'):
    prediccion = modelo_regresion.predict(nuevos_datos_procesados)
    
    # Mostrar el resultado
    st.write(f"La predicción del modelo es: {prediccion[0]:.2f}")