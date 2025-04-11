from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class GameConcept(models.Model):
    GENRE_CHOICES = [
        ('RPG', 'RPG'),
        ('FPS', 'FPS'),
        ('Strategy', 'Strategy'),
        ('Adventure', 'Adventure'),
        ('Horror', 'Horror'),
        ('Platformer', 'Platformer'),
        ('Puzzle', 'Puzzle'),
        ('Other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    ambiance = models.CharField(max_length=200)
    keywords = models.JSONField(default=list)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='game_concepts/', null=True, blank=True)
    
    def __str__(self):
        return self.title

class GameUniverse(models.Model):
    concept = models.OneToOneField(GameConcept, on_delete=models.CASCADE, related_name='universe')
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Univers de {self.concept.title}"

class GameStory(models.Model):
    concept = models.OneToOneField(GameConcept, on_delete=models.CASCADE, related_name='story')
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Histoire de {self.concept.title}"

class GameCharacter(models.Model):
    concept = models.ForeignKey(GameConcept, on_delete=models.CASCADE, related_name='characters')
    name = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.concept.title}"