import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from PIL import Image
import json
import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie


from datetime import datetime

# Obtenir la date et l'heure actuelle
now = datetime.now()





# Chemin vers le fichier JSON de configuration téléchargé depuis Firebase Console
cred = credentials.Certificate('appweb-dd4ba-292184362c6f.json')

# Vérifier si l'application Firebase a déjà été initialisée
if not firebase_admin._apps:
    # Initialisation de l'application Firebase
    firebase_admin.initialize_app(cred)


def Acceuil():

    image = "./Mini-serre_00_1.jpg"  # Remplacez l'URL par l'URL de votre image
    st.image(image, use_column_width=True)
    st.markdown("""
    <div style="text-align:center; font-weight:bold; font-size:40px;">
        Welcome to our <span style="color:green;">GreenBox</span> project
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center;">
        In the GreenBox project, we are developing a machine learning-based tool for detecting 
        foliar diseases in tomato plants. Our objective is to provide farmers with a practical 
        and reliable solution for diagnosing these diseases. By utilizing advanced algorithms 
        and data analysis techniques, we aim to accurately identify the specific diseases affecting tomato plants. 
        This will enable farmers to take timely and appropriate measures to treat and prevent further spread 
        of the diseases. 
    </div>
    """, unsafe_allow_html=True)

def home():
    st.title("Home")
    st.write("welcome to our web app for disease detection!")
    st.subheader("Upload Plant Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
   
    
    if uploaded_file is not None:
        # Afficher l'image téléchargée
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Plant Image', use_column_width=True)
        
        # Prédire la maladie de la plante
        #disease_name = predict_plant_disease(image)  # Supposons que cette fonction renvoie le nom de la maladie
        #st.write(f"Predicted Disease: {disease_name}")


    
def contact():
    st.header(":mailbox: Get In Touch With Me!")


    contact_form = """
    <form action="https://formsubmit.co/hibaoujaou@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


def capteurs():
    
    # Afficher la date et l'heure actuelle
    st.markdown(
    f"""
    <div style="background-color:#f0f0f0; padding:10px; border-radius:10px;text-align:center;">
        <p style="font-size:20px; color:#333; margin-bottom:10px;">
            <i class="far fa-calendar-alt" style="margin-right:10px;text-align:center;"></i>Date: {now.strftime("%Y-%m-%d")}
        </p>
        <p style="font-size:20px; color:#333;">
            <i class="far fa-clock" style="margin-right:10px;"></i>Heure: {now.strftime("%H:%M:%S")}
        </p>
    </div>
    """,
    unsafe_allow_html=True
    )
    st.title("Sensor Data Monitoring")
    st.markdown("In this page, you will find a visualization of the measurements captured by the humidity and temperature sensors."
                "This real-time visualization allows users to" 
                "closely monitor temperature and humidity fluctuations, facilitating informed and responsive decision-making")
    st.markdown('<div style="margin-top: 80px;"></div>', unsafe_allow_html=True)
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    lottie_coding = load_lottiefile("coding.json")
    lottie_humidity = load_lottiefile("humidity.json")

    


    # Créer deux colonnes pour placer les images
    col1, col2 = st.columns(2)
    
# Placer la première image dans la première colonne
    with col1:
        st_lottie(
            lottie_coding,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            height=200,
            width=200,
            key=None,
            
        )
       
    # Placer la deuxième image dans la deuxième colonne
    with col2:
        st_lottie(
            lottie_humidity,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            height=200,
            width=200,
            key=None,
        )
    # Créer un rectangle au centre de la page avec les mesures de température et d'humidité
    st.markdown("""
        <div style="width: 250px; height: 100px; background-color: #f0f0f0; 
                    border-radius: 10px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-left: 160px;">
            <div style="text-align:center;">Temperature: 28°C</div>
            <div style="text-align:center;">Humidity: 55%</div>
        </div>
    """, unsafe_allow_html=True)

    
def main():
    pages = {
        "Acceuil": Acceuil,
        "Home": home,
        "Sensor Data" : capteurs,
        "Contact" : contact,
        
    }

    st.sidebar.title("Navigation")
    page = st.sidebar.radio(" ", list(pages.keys()))

    # Exécutez la fonction de la page sélectionnée
    pages[page]()

if __name__ == "__main__":
    main()
