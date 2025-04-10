from django.db import models
from django.contrib.auth.models import User

class GameProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    ambiance = models.CharField(max_length=100)
    keywords = models.TextField()
    scenario = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
