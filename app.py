import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titre de l'application
st.title("🐔 Dashboard Plume d'Or")
st.subheader("Analyse des données de la ferme avicole")

# Données
data = {
    "Mois": ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"],
    "Ventes": [1200, 1800, 1500, 2200, 1900, 2500],
    "Charges": [800, 900, 850, 1000, 950, 1100]
}

df = pd.DataFrame(data)

# Afficher le tableau
st.subheader("📊 Tableau des données")
st.dataframe(df)

# Graphique
st.subheader("📈 Évolution des ventes")
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df["Mois"], df["Ventes"], color="green", marker="o")
ax.set_xlabel("Mois")
ax.set_ylabel("Ventes (FCFA)")
ax.grid(True)
st.pyplot(fig)
