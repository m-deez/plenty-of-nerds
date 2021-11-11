from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Nerd

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class NerdList(TemplateView):
    template_name = "nerd_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["nerds"] = Nerd.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["nerds"] = Nerd.objects.all()
            context["header"] = "Checkout These Nerds"
        return context