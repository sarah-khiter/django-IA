# GameForge - Générateur de Concepts de Jeux Vidéo avec IA

Application web permettant de générer automatiquement des concepts de jeux vidéo grâce à l'IA. Génération d'univers, d'histoires, de personnages et d'images conceptuelles.

## Fonctionnalités Principales

- 🎮 Génération de concepts de jeux complets
- 🌌 Création d'univers détaillés
- 📖 Génération d'histoires captivantes
- 👥 Description des personnages
- 🎨 Génération d'images conceptuelles
- 🔐 Système d'authentification sécurisé

## Stack Technique

### Backend
- Django, PostgreSQL, Python

### Frontend
- HTML5/CSS3, Bootstrap 5

### IA & APIs
- Hugging Face (Mistral-7B-Instruct & Stable Diffusion)

## APIs et Modèles IA

### Génération de Texte (Mistral-7B-Instruct)
- **Univers du Jeu** : Prompt structuré incluant titre, genre, ambiance et mots-clés
- **Histoire** : Génération narrative basée sur le contexte du jeu
- **Personnages** : Création de profils détaillés avec apparence, personnalité et rôle

### Génération d'Images (Stable Diffusion)
- **Images Conceptuelles** : 
  - Prompt : Combinaison du titre, genre, ambiance et mots-clés
  - Paramètres : 
    - num_inference_steps: 30
    - guidance_scale: 7.5
    - negative_prompt: "ugly, blurry, poor quality, distorted"

## Installation

```bash
git clone [URL_DU_REPO]
cd django-IA
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

Configuration du `.env` :
```
SECRET_KEY=votre_secret_key
DEBUG=True
HUGGINGFACE_API_KEY=votre_clé_api
```

## Sécurité

- 🔒 Authentification utilisateur avec Django
- 🔑 Gestion sécurisée des mots de passe
- 🛡️ Protection CSRF
- 🔐 Variables d'environnement pour les clés API
- 🔒 Accès restreint aux fonctionnalités (login_required)
- 🛡️ Validation des données côté serveur

## Utilisation

1. Création de compte
2. Connexion sécurisée
3. Génération de concept
4. Visualisation des résultats

## Structure

```
django-IA/
├── gameforge/
│   ├── core/           # App principale
│   ├── projects/       # Gestion projets
│   ├── users/          # Authentification
│   ├── templates/      
│   └── static/         
├── media/              
└── requirements.txt    
```


