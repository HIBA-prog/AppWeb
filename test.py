import streamlit as st
from twilio.rest import Client

# Configuration Twilio (remplacez les valeurs par vos propres clés et tokens)
TWILIO_ACCOUNT_SID = "US7cc80b1cdb759ab0b464f8d1f636f3f8"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "+212659961424"

# Initialisation du client Twilio
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Fonction pour envoyer un SMS
def send_sms(message, to):
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        st.success("Message sent successfully!")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Interface utilisateur Streamlit
st.title("Send SMS from Streamlit")

# Champ de saisie pour le message et le numéro de téléphone
message = st.text_input("Enter your message:")
phone_number = st.text_input("Enter the phone number (with country code):")

# Bouton pour envoyer le SMS
if st.button("Send SMS"):
    if message and phone_number:
        send_sms(message, phone_number)
    else:
        st.warning("Please enter both message and phone number.")
