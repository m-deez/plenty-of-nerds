from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Nerd, Game
from .forms import GameForm, GameDeleteForm

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

class GameList(TemplateView):
    template_name = "game_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context["games"] = Game.objects.filter(title__icontains=title)
            context["header"] = f"Searching for {title}"
        else:
            context["games"] = Game.objects.all()
            context["header"] = "Checkout These Games"
        return context

def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_create')
    else:
        form = GameForm()
    return render(request,
                  'game_create.html',
                  {
                      'form': form
                  })

def game_edit(request, pk=None):
    post = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = GameForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('game_create')
    else:
        form = GameForm(instance=post)

    return render(request,
                  'game_edit.html',
                  {
                      'form': form,
                      'post': post
                  })


def game_delete(request, pk=None):
    post = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = GameDeleteForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect('game_create')
    else:
        form = GameDeleteForm(instance=post)

    return render(request, 'game_delete.html',
                  {
                      'form': form,
                      'post': post,
                  })