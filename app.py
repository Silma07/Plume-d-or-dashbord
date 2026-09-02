import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Silma Dashboard",
    page_icon="💍",
    layout="wide"
)

st.title("💍 Dashboard Silma")
st.subheader("Boutique de bijoux en ligne")
#  Données ventes 
ventes = {
    "Produit": ["Bagues", "Boucles d'oreilles", "Bracelets", 
                "Colliers", "Ensembles bracelets", "Ensembles collier+boucles"],
    "Qté Juillet": [90, 12, 6, 6, 0, 0],
    "Revenu Juillet": [108000, 18000, 15000, 18000, 0, 0],
    "Qté Août": [30, 11, 15, 4, 16, 3],
    "Revenu Août": [36000, 22000, 37500, 12000, 120000, 12000]
}
df_ventes = pd.DataFrame(ventes)

# Données charges 
charges = {
    "Catégorie": ["Matières premières", "Livraison", 
                  "Publicité TikTok", "Emballage", "Autres"],
    "Juillet": [50000, 11500, 0, 25000, 4000],
    "Août": [10000, 22750, 0, 0, 4000]
}
df_charges = pd.DataFrame(charges)

# Calculs 
total_juillet = df_ventes["Revenu Juillet"].sum()
total_aout = df_ventes["Revenu Août"].sum()
charges_juillet = df_charges["Juillet"].sum()
charges_aout = df_charges["Août"].sum()
benefice_juillet = total_juillet - charges_juillet
benefice_aout = total_aout - charges_aout
#  Métriques principales 
st.markdown("---")
st.subheader("📊 Vue générale")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Ventes Juillet", f"{total_juillet:,} FCFA")

with col2:
    st.metric("💰 Ventes Août", f"{total_aout:,} FCFA",
              delta=f"{total_aout - total_juillet:,} FCFA")

with col3:
    st.metric("📈 Bénéfice Juillet", f"{benefice_juillet:,} FCFA")

with col4:
    st.metric("📈 Bénéfice Août", f"{benefice_aout:,} FCFA",
              delta=f"{benefice_aout - benefice_juillet:,} FCFA")
