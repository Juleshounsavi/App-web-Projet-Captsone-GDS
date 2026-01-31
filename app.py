import streamlit as st # type: ignore

# -------------------
# Fonctions
# -------------------
def calcul_carbone(duree_h, puissance_w, facteur_co2, materiel="CPU"):
    """
    Calcule l'empreinte carbone d'un entraînement ML selon le type de matériel.
    
    Paramètres:
        duree_h (float): durée d'entraînement en heures
        puissance_w (float): puissance nominale du matériel en Watts
        facteur_co2 (float): facteur d'émission en kgCO2/kWh
        materiel (str): "CPU" ou "GPU"
        
    Retourne:
        tuple: (energie_kwh, co2_kg)
    """
    # Ajuster la consommation selon le matériel
    if materiel.upper() == "GPU":
        puissance_w *= 2  # facteur approximatif : GPU consomme ~2x un CPU
    elif materiel.upper() != "CPU":
        raise ValueError("Type de matériel inconnu. Choisir 'CPU' ou 'GPU'.")
    
    energie_kwh = (puissance_w * duree_h) / 1000
    co2_kg = energie_kwh * facteur_co2
    return energie_kwh, co2_kg

def evaluation_impact(co2_kg):
    """
    Retourne une évaluation qualitative en fonction des émissions.
    """
    if co2_kg < 1:
        return "✅ Très faible impact (bonnes pratiques)"
    elif co2_kg < 5:
        return "⚠️ Impact modéré (acceptable, mais améliorable)"
    elif co2_kg < 20:
        return "🚨 Impact élevé (réduire si possible)"
    else:
        return "🌍🔥 Impact très élevé (à éviter absolument)"

# -------------------
# Interface Streamlit
# -------------------
st.title("🌱 Calculateur d'empreinte carbone ML")
st.write("Estimez la consommation énergétique et les émissions de CO₂ de votre entraînement ML.")

# Widgets pour les entrées
duree = st.number_input("Durée d'entraînement (heures)", min_value=0.0, value=1.0, step=0.1)
puissance = st.number_input("Puissance du matériel (Watts)", min_value=0.0, value=200.0, step=10.0)
facteur = st.number_input("Facteur d'émission (kgCO2/kWh)", min_value=0.0, value=0.233, step=0.001)
materiel = st.selectbox("Type de matériel", ["CPU", "GPU"])

# Bouton de calcul
if st.button("Calculer l'empreinte carbone"):
    energie, co2 = calcul_carbone(duree, puissance, facteur, materiel)
    
    st.metric("🔹 Énergie consommée (kWh)", f"{energie:.2f}")
    st.metric("🔹 Émissions estimées (kg CO₂)", f"{co2:.2f}")
    st.write(f"🔹 **Évaluation:** {evaluation_impact(co2)}")
    
    # Message supplémentaire selon l'impact
    if co2 >= 20:
        st.warning("⚠️ Attention : consommation très élevée. Pensez à optimiser vos entraînements ou utiliser du matériel plus efficace.")
