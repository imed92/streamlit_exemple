import streamlit as st # Ici on importe streamlit
from PIL import Image # On importe le module Image depuis la librairie PIL
import datetime
import pandas as pds # pandas est une librairie qui permet de manipuler des données
import plotly.express as px # Import de plotly express pour créer des graphiques interactifs
import plotly.graph_objects as go # Import de Graph objects pour des graphiques plus complexes


# Ci dessous je lis le fichier Adidas.xlsx et je stocke son contenu dans la variable df
df = pds.read_excel("Adidas.xlsx")

# Ici dans la configuration de base de streamlit, on utilise l'entiereté de l'écran
st.set_page_config(layout="wide") # Largeur

# Ici on définit la marge d'où on veut démarrer
st.markdown('<style>div.block-container{padding-top:4rem;}</style>', unsafe_allow_html=True) # Longueur en partant d'en haut

image = Image.open('adidas-logo.jpg') # Ici on stock l'image du logo de adidas

col1, col2 = st.columns([0.1, 0.9]) # Ici on créer les colonnes pour l'affichage de l'image et du titre
# Equivalent de ci dessous mais abrégé
# col1 = st.columns(0.1)
# col2 = st.columns(0.9)

# Ici on place l'image dans col1
with col1:
    st.image(image, width=100)

# Ici on définit le titre
title = "<center><h1>Adidas Dashboard</h1></center>"

# Ici on place le titre en haut au milieu de l'écran
with col2:
    st.markdown(title, unsafe_allow_html=True)


col3, col4, col5 = st.columns([0.1, 0.45, 0.45])

with col3:
    # Ci dessous je stock dans la variable box_date la date du jour au format jour, mois, année
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write("Dernière mise à jour le : \n"+box_date)


# Ici on va créer le graphique en barre des ventes des distributeur
with col4:
    # Dans fig on va stocker notre graphique en barre
    fig = px.bar(df, x="Retailer", y="TotalSales", labels={"TotalSales": "Total des ventes ($)", "Retailer" : "Revendeur"}, title="Total des ventes par revendeur", hover_data=["TotalSales"], template="gridon", height=500)
    # Ici on va afficher fig donc notre graphique qu'on a paramétré dans la ligne précédente
    st.plotly_chart(fig, use_container_width=True)