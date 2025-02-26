# ici on importe la librairie streamlit
import streamlit as st

# Ici on définit le titre de notre application web
st.title("Mon premier Dashboard avec Streamlit")
# On affiche une phrase de bienvenue toute simple
st.write("Bienvenue dans mon application interactive")

# La variable name ci dessous sera égale à la valeur que l'utilisateur aura tapé dans l'input
name = st.text_input("Entrez votre nom : ")

if name:
    st.write("Bonjour "+name)

number = st.slider("Choisissez un nombre :", 1, 100, 50)
st.write("Vous avez choisi : "+str(number))

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

# st.set_page_config(theme)