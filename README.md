# App-web-Projet-Captsone-GDS
App Streamlit pour estimation de l’empreinte carbone des entraînements de modèles de Machine Learning (ML) pour sensibiliser les étudiants et développeurs aux impacts environnementaux de leurs choix numériques.  


## 📄 Description

Cette application web interactive, développée avec **Python** et **Streamlit**, permet de :

- Calculer la **consommation énergétique** d’un entraînement ML (kWh)
- Estimer les **émissions de CO₂** correspondantes (kg CO₂)
- Fournir une **évaluation qualitative** de l’impact environnemental
- Prendre en compte le type de matériel utilisé (**CPU ou GPU**)
---

##  Fonctionnalités

1. Entrées interactives via **sliders** et **selectbox** :
    - Durée d’entraînement (heures)
    - Puissance du matériel (Watts)
    - Facteur d’émission (kgCO₂/kWh)
    - Type de matériel : CPU ou GPU

2. Calcul automatique de :
    - Energie consommée en kWh
    - Émissions de CO₂ en kg

3. Évaluation de l’impact avec **icônes et messages clairs** :
    - Très faible impact
    - Impact modéré
    - Impact élevé
    - Impact très élevé


## 🛠 Installation

1. **Cloner le dépôt** :

```bash
git clone https://github.com/<votre-utilisateur>/<nom-du-repo>.git
cd <nom-du-repo>
