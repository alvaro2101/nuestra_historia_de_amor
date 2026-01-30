import random
import streamlit as st
from PIL import Image
import base64
from datetime import date, datetime

# --- 1. FUNCIÓN DE FONDO (Definir al principio) ---
def agregar_fondo(nombre_archivo):
    with open(nombre_archivo, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    estilo = """
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.92); 
        border-radius: 25px;
        padding: 40px;
        box-shadow: 0 0 20px rgba(255, 183, 197, 0.5);
    }}

    /* TEXTO OSCURO (Excluyendo botones) */
    .stApp, .stMarkdown, p, h1, h2, h3, span, label, div:not(.stButton > button) {{
        color: #2c2c2c !important;
    }}

    /* BOTÓN ROSADO */
    div.stButton > button {{
        background-color: #FFB7C5 !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.6rem 2rem !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(255, 183, 197, 0.6) !important;
    }}

    @keyframes bubbles {{
        0% {{ bottom: -100px; transform: translateX(0); opacity: 0; }}
        50% {{ opacity: 0.8; }}
        100% {{ bottom: 100vh; transform: translateX(120px); opacity: 0; }}
    }}
    .heart {{
        position: fixed;
        bottom: -100px;
        font-size: 35px;
        z-index: 0; 
        animation: bubbles 35s linear infinite;
    }}
    </style>
    """.format(img=encoded_string)
    st.markdown(estilo, unsafe_allow_html=True)

# --- 2. FUNCIÓN DE LOGIN ---
def login():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if not st.session_state["autenticado"]:
        st.markdown("<h2 style='text-align: center;'>🔐 Acceso Privado</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            user = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")
            if st.button("Entrar ❤️"):
                if user == "Amor" and password == "300725":
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Datos incorrectos 🥺")
        return False
    return True

# Solo si el login es exitoso, se muestra el resto de la página
if login(): 
        def agregar_fondo(nombre_archivo):
         with open(nombre_archivo, "rb") as image_file:
          encoded_string = base64.b64encode(image_file.read()).decode()
    
          estilo = """
    <style>
    /* Fondo y Tarjeta */
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.92); 
        border-radius: 25px;
        padding: 40px;
        box-shadow: 0 0 20px rgba(255, 183, 197, 0.5);
    }}

    /* Texto Oscuro - Excluimos explícitamente los botones */
    .stApp, .stMarkdown, p, span, label, div:not(.stButton > button) {{
        color: #2c2c2c !important;
    }}

    /* El Botón Rosado Perfecto */
    div.stButton > button {{
        background-color: #FFB7C5 !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.6rem 2rem !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(255, 183, 197, 0.6) !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    /* Títulos con Glow */
    h1, h2, h3 {{
        color: #2c2c2c !important;
        text-shadow: 0 0 10px rgba(255, 183, 197, 0.8);
    }}

    /* Corazones Lentos */
    @keyframes bubbles {{
        0% {{ bottom: -100px; transform: translateX(0); opacity: 0; }}
        50% {{ opacity: 0.8; }}
        100% {{ bottom: 100vh; transform: translateX(120px); opacity: 0; }}
    }}
    .heart {{
        position: fixed;
        bottom: -100px;
        font-size: 35px;
        z-index: 0; 
        animation: bubbles 35s linear infinite;
    }}
    </style>
    """.format(img=encoded_string)
    
         st.markdown(estilo, unsafe_allow_html=True)

# Luego ejecutas la función
agregar_fondo('anime2.jpg')
# Esto crea 15 corazones que van saliendo poco a poco
import random
emojis = ["❤️", "💖", "✨", "🌸"]
for i in range(20): # Subimos a 20 para que se vea más lleno
    delay = i * 1.5
    size = random.randint(20, 40) # Tamaños aleatorios
    emoji = random.choice(emojis)
    st.markdown(f'<div class="heart" style="left: {i*5}%; animation-delay: {delay}s; font-size: {size}px;">{emoji}</div>', unsafe_allow_html=True)
# 1. Configuración de la página
st.set_page_config(
    page_title="Nuestra Historia Juntos",
    page_icon="❤️",
    layout="centered"
)

# --- NUEVO: SECCIÓN DE MÚSICA ---
# Asegúrate de tener un archivo llamado 'cancion.mp3' en la misma carpeta
# Si tu archivo tiene otro nombre, cámbialo aquí abajo.
# --- SECCIÓN DE MÚSICA OPTIMIZADA ---
st.sidebar.title("Nuestra Canción 🎵")
try:
    with open("cancion.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
    
    # Creamos un botón. Cuando ella haga clic, se activa el audio.
    if st.button("❤️ Haz clic para empezar la sorpresa ❤️"):
        st.audio(audio_bytes, format='audio/mp3', autoplay=True)
except FileNotFoundError:
    st.sidebar.warning("⚠️ No encontré el archivo 'cancion.mp3'.")
# -------------------------------

st.title("❤️ Feliz Aniversario, Amor ❤️")
st.write("He creado esta cápsula del tiempo para recordar nuestros mejores momentos.")
st.write("---")


from datetime import date, datetime

# --- CONFIGURACIÓN DEL CONTADOR ---
# CAMBIA ESTA FECHA por la de ustedes (Año, Mes, Día)
fecha_inicio = date(2025, 7, 30)  
fecha_hoy = date.today()

delta = fecha_hoy - fecha_inicio
years = delta.days // 365
months = (delta.days % 365) // 30
days = (delta.days % 365) % 30

# Mostramos el contador con métricas grandes
st.write(f"### Llevamos juntos: {delta.days} días ❤️")
# Mostramos el contador con estilo de tarjetas
st.write(f"### ❤️ Llevamos juntos:")

col1, col2, col3 = st.columns(3)

# Estilo para las métricas
estilo_metrica = """
    <div style="
        background-color: #FFB7C5; 
        padding: 20px; 
        border-radius: 15px; 
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    ">
<h2 style="color: white !important; margin: 0;">{valor}</h2>
<p style="color: white !important; margin: 0; font-weight: bold;">{etiqueta}</p>
    </div>
"""

with col1:
    st.markdown(estilo_metrica.format(valor=years, etiqueta="Años"), unsafe_allow_html=True)
with col2:
    st.markdown(estilo_metrica.format(valor=months, etiqueta="Meses"), unsafe_allow_html=True)
with col3:
    st.markdown(estilo_metrica.format(valor=days, etiqueta="Días"), unsafe_allow_html=True)

st.write("---")

# 3. Datos de la historia (Aquí es donde editarás luego)
# Puedes agregar tantos momentos como quieras a esta lista
momentos = [
    {
        "fecha": "30/07/25",
        "titulo": "El inicio de todo",
        "descripcion": "En el momento en el te entrege la carta y te di la cadenita, estaba muy nervioso.",
        "icono": "❤️",
        "foto": "mes1.jpg"
    },
    {
        "fecha": "30/08/25",
        "titulo": "Nuestro primer mes",
        "descripcion": "Poco a poco nos fuimos conociendo, aunque a la vista de todos parece que vamos muy rapido para mi eres lo mejor que Dios me a dado.",
        "icono": "❤️"
    },
    {
        "fecha": "30/09/25",
        "titulo": "Nuestro segundo mes",
        "descripcion": "Fue nuestra cita al cine, fuimos a ver KNY como buenos otakus jsjsjsj.",
        "icono": "❤️",
        "foto": "cine.jpg"
    },
    {
        "fecha": "30/10/25",
        "titulo": "Nuestro tercer mes ",
        "descripcion": "Algunas peleas a lo largo de nuestra relacion, pero nada que no lo podriamos superar juntos.",
        "icono": "❤️",
        "foto": "pelea.jpg"
    },
    {
        "fecha": "30/11/25",
        "titulo": "Nuestro cuarto mes",
        "descripcion": "Gracias por cada día juntos, me enseñas a quererte cada dia un poco mas.",
        "icono": "❤️",
        "foto": "mary.jpg"
    },
    {
        "fecha": "30/12/25",
        "titulo": "Nuestro quinto mes",
        "descripcion": "Aunque navidad la pasamos cada uno en su casita, me encantó pasar año nuevo a tu lado.",
        "icono": "❤️",
        "foto": "añon.jpg"
    },
    {
        "fecha": "30/01/26",
        "titulo": "Nuestro medio año mi amor",
        "descripcion": "Este mes no nos vimos mucho mi niña, pero aunque la distancia nos separa el amor sigue siendo muy fuerte.",
        "icono": "❤️"
    }

]

# 4. Lógica para mostrar la línea de tiempo
for evento in momentos:
    with st.container():
        col1, col2 = st.columns([1, 5])
        with col1:
            st.header(evento["icono"])
        with col2:
            st.subheader(f"{evento['fecha']} - {evento['titulo']}")
            st.write(evento["descripcion"])
            
            # --- NUEVO: Mostrar foto si existe ---
            if "foto" in evento:
                # Esto crea el efecto de bordes redondeados y sombra
                st.markdown(
                    f"""
                    <style>
                    .portaretrato {{
                        border-radius: 20px;
                        border: 5px solid #FFB7C5;
                        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
                    }}
                    </style>
                    <img src="data:image/png;base64,{base64.b64encode(open(evento["foto"], "rb").read()).decode()}" class="portaretrato" width="300">
                    """, 
                    unsafe_allow_html=True
                )
                
    st.divider()

# 5. Un detalle final en la barra lateral
st.sidebar.title("Dedicatoria")
st.sidebar.write("Creado con mucho amor y Python para ti.")
st.header("¿Por qué te elijo cada día?")
if st.button("Dime una razón ❤️"):
    razones = [
        "Por cómo te brillan los ojos cuando te ríes.",
        "Porque no imagino un 'mañana' sin ti.",
        "Porque nuestro amor es un proyecto que quiero cuidar siempre.",
        "No te elijo por necesidad, sino porque mi libertad se siente más completa cuando la comparto contigo.",
        "Porque haces mi mundo mejor.",
        "Por tu paciencia infinita conmigo.",
        "Simplemente porque eres tú."
        "Porque te amo muchooo mi niña"
        "Porque eres mia :3 "
    ]
    # Elige una al azar y la muestra
    st.success(random.choice(razones))

st.write("---")
with st.expander("✉️ Un mensaje secreto para ti..."):
    st.write("""
    TE AMO MUCHO, quiero pasar toda la vida contigo amor, espero que esto sea un para siempre mi niña.
    """)
 