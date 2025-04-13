import os
import requests
import json
import logging
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration de l'API Hugging Face
logger.info("Chargement de la clé API Hugging Face...")
API_KEY = os.getenv('HUGGINGFACE_API_KEY')
logger.info(f"Valeur de HUGGINGFACE_API_KEY: {API_KEY}")

if not API_KEY:
    logger.error("HUGGINGFACE_API_KEY n'est pas définie dans les variables d'environnement")
    raise ValueError("HUGGINGFACE_API_KEY n'est pas définie dans les variables d'environnement")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
logger.info("Configuration de l'API Hugging Face terminée")

# Configuration de l'API Hugging Face
# Utilisation du modèle Mistral pour la génération de texte
TEXT_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
IMAGE_API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

# Configuration des paramètres de génération pour Mistral
GPT_PARAMS = {
    "max_length": 500,  # Longueur maximale du texte généré
    "do_sample": True,  # Active la génération créative
    "temperature": 0.7,  # Contrôle le niveau de créativité
    "top_k": 50,  # Nombre de tokens à considérer
    "top_p": 0.95,  # Probabilité cumulative
    "repetition_penalty": 1.2  # Évite la répétition
}

# Modèles
TEXT_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"  # Modèle Mistral
IMAGE_MODEL = "CompVis/stable-diffusion-v1-4"

def generate_content(prompt, max_length=500):
    """
    Génère du contenu texte à partir d'un prompt en utilisant GPT-2.
    
    Args:
        prompt (str): Le texte d'entrée pour la génération
        max_length (int): Longueur maximale du texte généré
        
    Returns:
        str: Le texte généré ou None en cas d'erreur
    """
    try:
        # Préparation des paramètres pour la requête API
        payload = {
            "inputs": prompt,
            "parameters": GPT_PARAMS
        }
        
        # Envoi de la requête POST à l'API
        response = requests.post(TEXT_API_URL, headers=HEADERS, json=payload)
        
        # Vérification que la requête a réussi
        response.raise_for_status()
        
        # Extraction et retour du texte généré
        return response.json()[0]['generated_text']
        
    except Exception as e:
        # Journalisation de l'erreur en cas d'échec
        logger.error(f"Erreur lors de la génération de texte avec GPT: {str(e)}")
        return None

def generate_game_universe(concept):
    """
    Génère la description de l'univers du jeu.
    
    Args:
        concept (GameConcept): L'instance du concept de jeu
        
    Returns:
        str: La description de l'univers générée
    """
    # Construction du prompt détaillé pour la génération de l'univers
    prompt = f"""En tant qu'expert en design de jeux vidéo, décrivez l'univers du jeu suivant :
    Titre: {concept.title}
    Genre: {concept.genre}
    Ambiance: {concept.ambiance}
    Mots-clés: {', '.join(concept.keywords)}
    
    Décrivez l'univers en détail, incluant :
    - L'environnement principal
    - L'atmosphère générale
    - Les éléments uniques
    - Les règles du monde"""
    
    # Appel à la fonction de génération de contenu
    return generate_content(prompt)

def generate_story(concept):
    """
    Génère l'histoire principale du jeu.
    
    Args:
        concept (GameConcept): L'instance du concept de jeu
        
    Returns:
        str: L'histoire générée
    """
    # Construction du prompt détaillé pour la génération de l'histoire
    prompt = f"""En tant que scénariste de jeux vidéo, créez l'histoire du jeu suivant :
    Titre: {concept.title}
    Genre: {concept.genre}
    Ambiance: {concept.ambiance}
    
    Développez une histoire captivante incluant :
    - Le contexte initial
    - Le conflit principal
    - Les objectifs du joueur
    - Les enjeux"""
    
    # Appel à la fonction de génération de contenu
    return generate_content(prompt)

def generate_characters(concept):
    """
    Génère les descriptions des personnages principaux.
    
    Args:
        concept (GameConcept): L'instance du concept de jeu
        
    Returns:
        str: Les descriptions des personnages générées
    """
    # Construction du prompt détaillé pour la génération des personnages
    prompt = f"""En tant que concepteur de personnages, créez les personnages principaux pour le jeu :
    Titre: {concept.title}
    Genre: {concept.genre}
    Ambiance: {concept.ambiance}
    
    Décrivez les personnages principaux, incluant pour chacun :
    - Leur apparence
    - Leur personnalité
    - Leur rôle dans l'histoire
    - Leurs motivations"""
    
    # Appel à la fonction de génération de contenu
    return generate_content(prompt)

def generate_image(prompt, negative_prompt=None):
    """
    Génère une image avec l'API Hugging Face.
    
    Args:
        prompt (str): La description de l'image à générer
        negative_prompt (str, optional): Ce qu'il faut éviter dans l'image
        
    Returns:
        ContentFile: Le fichier image généré ou None en cas d'erreur
    """
    try:
        logger.info(f"Début de la génération d'image avec le prompt: {prompt}")
        
        # Vérification de la clé API
        if not API_KEY:
            logger.error("HUGGINGFACE_API_KEY n'est pas définie")
            return None
            
        # Préparation du payload
        payload = {
            "inputs": prompt,
            "parameters": {
                "num_inference_steps": 30,
                "guidance_scale": 7.5,
                "negative_prompt": negative_prompt or "ugly, blurry, poor quality, distorted"
            }
        }
        
        logger.info("Envoi de la requête à l'API...")
        response = requests.post(
            IMAGE_API_URL,
            headers=HEADERS,
            json=payload
        )
        
        # Vérification de la réponse
        if response.status_code == 200:
            logger.info("Image générée avec succès")
            return ContentFile(response.content, name=f"{prompt[:20]}.png")
        else:
            logger.error(f"Erreur API: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        logger.error(f"Erreur lors de la génération d'image: {str(e)}")
        return None 