import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Mon Outil Interactif", page_icon="🚀", layout="wide")

# --- TITRE PRINCIPAL ---
st.title("🚀 Interface de mon Super Outil")
st.markdown("Bienvenue ! Utilisez les options ci-dessous pour interagir avec l'outil.")

# --- BARRE LATÉRALE (SIDEBAR) POUR LES PARAMÈTRES ---
with st.sidebar:
    st.header("⚙️ Paramètres")
    modele_choisi = st.selectbox(
        "Choisissez un mode de traitement :",
        ("Rapide", "Précis", "Expérimental")
    )
    seuil = st.slider("Réglez la sensibilité (Seuil) :", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
    st.info("Ces paramètres modifient le comportement de l'outil.")

# --- ZONE PRINCIPALE : ENTRÉES UTILISATEUR ---
st.subheader("📥 Entrez vos données")

col1, col2 = st.columns(2) # Création de deux colonnes pour un design plus propre

with col1:
    texte_utilisateur = st.text_area("Saisissez votre texte ou requête ici :", "Exemple de texte...")

with col2:
    fichier_upload = st.file_uploader("Ou importez un fichier (CSV, TXT...)", type=['csv', 'txt'])

# --- BOUTON D'ACTION ---
st.markdown("---") # Ligne de séparation
bouton_lancer = st.button("⚡ Lancer le traitement", use_container_width=True)

# --- LOGIQUE DE L'OUTIL (Ce qui se passe quand on clique) ---
if bouton_lancer:
    if not texte_utilisateur and fichier_upload is None:
        st.warning("Veuillez entrer du texte ou charger un fichier avant de lancer.")
    else:
        # Affichage d'un spinner pendant le "calcul"
        with st.spinner("L'outil travaille en coulisse... Veuillez patienter."):
            
            # ---> C'EST ICI QUE VOUS METTEZ LE CODE DE VOTRE OUTIL <---
            time.sleep(2) # Simule un temps de traitement (à remplacer par votre code)
            
            # --- AFFICHAGE DES RÉSULTATS ---
            st.success("Traitement terminé avec succès !")
            
            st.subheader("📊 Résultats")
            
            # Exemple 1 : Afficher du texte
            st.write(f"**Mode utilisé :** {modele_choisi} | **Seuil :** {seuil}")
            st.write(f"**Longueur de votre texte :** {len(texte_utilisateur)} caractères.")
            
            # Exemple 2 : Afficher un tableau de données (Généré aléatoirement pour l'exemple)
            st.markdown("#### Tableau de données généré :")
            donnees_resultat = pd.DataFrame(
                np.random.randn(10, 3),
                columns=['Score A', 'Score B', 'Tendance']
            )
            st.dataframe(donnees_resultat, use_container_width=True)
            
            # Exemple 3 : Afficher un graphique
            st.markdown("#### Visualisation :")
            st.line_chart(donnees_resultat)
