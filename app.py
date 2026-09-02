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
# ── Graphiques ───────────────────────────────────────────────
st.markdown("---")
st.subheader("📈 Analyse des ventes")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Ventes par produit — Juillet**")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    df_ventes_juillet = df_ventes[df_ventes["Revenu Juillet"] > 0]
    ax1.barh(df_ventes_juillet["Produit"], 
             df_ventes_juillet["Revenu Juillet"],
             color="#C8A96E")
    ax1.set_xlabel("Revenu (FCFA)")
    ax1.grid(axis="x")
    st.pyplot(fig1)

with col2:
    st.markdown("**Ventes par produit — Août**")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    df_ventes_aout = df_ventes[df_ventes["Revenu Août"] > 0]
    ax2.barh(df_ventes_aout["Produit"],
             df_ventes_aout["Revenu Août"],
             color="#8B5E3C")
    ax2.set_xlabel("Revenu (FCFA)")
    ax2.grid(axis="x")
    st.pyplot(fig2)

# Évolution mensuelle
st.markdown("**📊 Évolution mensuelle — Revenus vs Charges**")
fig3, ax3 = plt.subplots(figsize=(10, 4))
mois = ["Juillet", "Août"]
ax3.plot(mois, [total_juillet, total_aout], 
         color="#C8A96E", marker="o", linewidth=2, label="Revenus")
ax3.plot(mois, [charges_juillet, charges_aout],
         color="#E74C3C", marker="o", linewidth=2, label="Charges")
ax3.plot(mois, [benefice_juillet, benefice_aout],
         color="#2ECC71", marker="o", linewidth=2, label="Bénéfice")
ax3.legend()
ax3.grid(True)
ax3.set_ylabel("FCFA")
st.pyplot(fig3)
