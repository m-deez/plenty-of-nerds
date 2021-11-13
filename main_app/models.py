from django.db import models
from django.db.models.deletion import CASCADE

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

class System(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return self.name

class XPL(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return self.name

class GameStyle(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=99)
    system = models.ForeignKey(System, on_delete=models.SET_NULL, blank=True, null=True)
    experience_lvl = models.ForeignKey(XPL, on_delete=models.SET_NULL, blank=True, null=True)
    players = models.IntegerField()
    gm_required = models.BooleanField(default=False)
    game_style = models.ForeignKey(GameStyle, on_delete=models.SET_NULL, blank=True, null=True)
    about = models.TextField()
    nerd = models.ForeignKey(Nerd, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']