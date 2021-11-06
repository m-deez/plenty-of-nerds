from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Nerd:
    def __init__(self, gm, name, img, bio, questionnaire):
        self.gm = gm
        self.name = name
        self.img = img
        self.bio = bio
        self.questionnaire = questionnaire

nerds = [
    Nerd("yes", "Dingus", "https://i.imgur.com/B04AVJZ.jpeg", "I am a DM. Bow to me!", "Something something questionnaire."),
    Nerd("no", "Dongus", "https://i.imgur.com/T0WlDmD.jpeg", "I am a lowly player with doodoo for brains.", "Questionnaire?! No one said anything about a questionnaire!")
]

class NerdList(TemplateView):
    template_name = "nerd_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nerds"] = nerds
        return context