from django.db import models

# Create your models here.

class Nerd(models.Model):
    gm = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Game(models.Model):
    title = models.CharField(max_length=99)
    system = models.CharField(max_length=100)
    experience_lvl = models.CharField(max_length=100)
    players = models.CharField(max_length=100)
    gm_required = models.BooleanField(default=False)
    game_style = models.CharField(max_length=100)
    about = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']