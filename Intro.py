import streamlit as st
from PIL import Image

st.title("Aplicaciones De mi portafolio.")

# Configuración de la barra lateral
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# Enlace general
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# Distribución en 3 columnas
col1, col2, col3 = st.columns(3)

# ------------------- COLUMNA 1 -------------------
with col1:
    st.subheader("Descenso del Gradiente")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write("Demostración interactiva sobre optimización y ajuste de parámetros mediante el algoritmo de descenso del gradiente.") 
    url1 = "https://appgradiente-eifxnarapplztndnmko8uqw.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url1})")

    st.subheader("Modelos de Regresión")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("Aplicación para el ajuste y análisis de modelos de regresión lineal y polinomial en conjuntos de datos.") 
    url2 = "https://appregresion-rvyrps9sawmnrvcdmmc4m2.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url2})")

    st.subheader("Series de Tiempo")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("Análisis, pronóstico y detección de estacionalidad y tendencias en datos secuenciales a lo largo del tiempo.") 
    url3 = "https://seriestiempo-5gzexmbwvvbvstvtgmqp2s.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url3})")

    st.subheader("Conceptos de IA")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("Módulo didáctico interactivo con los conceptos fundamentales y teóricos sobre la Inteligencia Artificial.") 
    url8 = "https://conceptos-c2iappkmghqepxebtffusgc.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url8})")

# ------------------- COLUMNA 2 -------------------
with col2: 
    st.subheader("Nivel de Agua - CORNARE")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("Monitoreo e interpretación analítica de los niveles de agua y caudales reportados por la entidad ambiental CORNARE.") 
    url4 = "https://nivelcornare-nkwj5yutes49lh4omnuntp.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url4})")

    st.subheader("Procesamiento de Datos")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("Herramienta interactiva para el análisis exploratorio, filtrado y modelado analítico de información.") 
    url5 = "https://ccbqiur6vrpf9qoqvix6xc.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url5})")

    st.subheader("Clasificación de Frutas")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("Modelo de visión por computadora para la detección e identificación automática de distintos tipos de fruta.") 
    url9 = "https://clasfruta-beyfd2nayf9nyfoicovwla.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url9})")

# ------------------- COLUMNA 3 -------------------
with col3: 
    st.subheader("Modelo Predictivo")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("Despliegue de modelos predictivos avanzados orientados a la toma de decisiones con datos.") 
    url6 = "https://2syfexf8u8j3pqhdmkwxhy.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url6})")

    st.subheader("Sistema IoT - Humedad")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Aplicación ciberfísica para la recolección y visualización en tiempo real de datos de humedad mediante sensores IoT.") 
    url7 = "https://iot-humedad-fi685wxkxrr4zxdubwq9zg.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url7})")

    st.subheader("Clasificación de Faltas")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("Sistema de clasificación para la detección, categorización y registro de faltas o patrones atípicos.") 
    url10 = "https://clasefalta-dpkjsbcjanckjsnrugupkv.streamlit.app/"
    st.write(f"Ver App: [Enlace]({url10})")
