from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import GameConcept, GameUniverse, GameStory, GameCharacter
from .ai_generation import generate_game_universe, generate_story, generate_characters, generate_image
import json
import logging

logger = logging.getLogger(__name__)

@login_required
def game_concept_list(request):
    concepts = GameConcept.objects.filter(user=request.user)
    return render(request, 'core/game_concept_list.html', {'concepts': concepts})

@login_required
def game_concept_detail(request, pk):
    try:
        concept = get_object_or_404(GameConcept, pk=pk)
        # Vérifier que l'utilisateur a accès à ce concept
        if concept.user != request.user:
            messages.error(request, "Vous n'avez pas accès à ce concept de jeu.")
            return redirect('core:game_concept_list')
            
        universe = get_object_or_404(GameUniverse, concept=concept)
        story = get_object_or_404(GameStory, concept=concept)
        characters = GameCharacter.objects.filter(concept=concept)
        
        return render(request, 'core/game_concept_detail.html', {
            'concept': concept,
            'universe': universe,
            'story': story,
            'characters': characters
        })
    except Exception as e:
        logger.error(f"Erreur dans game_concept_detail: {str(e)}")
        messages.error(request, "Une erreur est survenue lors de l'affichage du concept.")
        return redirect('core:game_concept_list')

@login_required
def create_game_concept(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        ambiance = request.POST.get('ambiance')
        keywords = request.POST.get('keywords', '').split(',')
        
        try:
            # Création du concept
            concept = GameConcept.objects.create(
                title=title,
                genre=genre,
                ambiance=ambiance,
                keywords=keywords,
                user=request.user
            )
            
            # Génération de l'univers
            universe_description = generate_game_universe(concept)
            GameUniverse.objects.create(
                concept=concept,
                description=universe_description
            )
            
            # Génération de l'histoire
            story_description = generate_story(concept)
            GameStory.objects.create(
                concept=concept,
                description=story_description
            )
            
            # Génération des personnages
            characters_description = generate_characters(concept)
            GameCharacter.objects.create(
                concept=concept,
                description=characters_description
            )
            
            # Génération de l'image conceptuelle
            image_prompt = f"{title}, {genre}, {ambiance}, {', '.join(keywords)}"
            image_data = generate_image(image_prompt)
            if image_data:
                concept.image.save(f"{concept.id}.png", image_data, save=True)
            
            messages.success(request, 'Concept de jeu créé avec succès !')
            return redirect('core:game_concept_detail', pk=concept.id)
            
        except Exception as e:
            logger.error(f"Erreur lors de la création du concept: {str(e)}")
            messages.error(request, f'Erreur lors de la création du concept : {str(e)}')
            return redirect('core:game_concept_list')
    
    return render(request, 'core/create_game_concept.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Inscription réussie ! Bienvenue sur GameForge.')
            return redirect('core:game_concept_list')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def logout_view(request):
    """Vue pour la déconnexion de l'utilisateur"""
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('core:game_concept_list')