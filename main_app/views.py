from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Nerd, Game
from .forms import GameForm, GameDeleteForm
import time

# Create your views here.

# Splash page views ----------------------------------------------------------------->
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

# User views ------------------------------------------------------------------------>
@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class NerdCreate(CreateView):
    model = Nerd
    fields = ['gm', 'name', 'img', 'bio']
    template_name = "nerd_create.html" 
    success_url = "/"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NerdCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class NerdDetails(DetailView):
    model = Nerd
    template_name = "nerd_details.html"
    
@method_decorator(login_required, name='dispatch')
class UserDetails(DetailView):
    model = Nerd
    template_name = "user_nerd_details.html"

@method_decorator(login_required, name='dispatch')
class NerdUpdate(UpdateView):
    model = Nerd
    fields = ["gm", "name", "img", "bio"]
    template_name = "nerd_update.html"
    
    def get_success_url(self):
        return reverse('user_nerd_details', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class NerdDelete(DeleteView):
    model = Nerd
    template_name = "nerd_delete_confirmation.html"
    success_url = "/accounts/signup/"

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("nerd_create")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

# Game views ------------------------------------------------------------------------->
@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class GameDetails(DetailView):
    model = Game
    template_name = "game_details.html"

def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request,
                  'game_create.html',
                  {
                      'form': form,
                  })

def game_edit(request, pk=None):
    post = get_object_or_404(Game, pk=pk)
    form = GameForm(instance=post)
    if request.method == "POST":
        form = GameForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('game_details', pk=pk)
    else:
        form = GameForm(instance=post)

    return render(request,
                  'game_edit.html',
                  {
                      'form': form,
                      'post': post
                  })

@method_decorator(login_required, name='dispatch')
class GameDelete(DeleteView):
    model = Game
    template_name = "game_delete.html"
    success_url = "/games/"

# def game_delete(request, pk=None):
#     post = get_object_or_404(Game, pk=pk)
#     form = GameDeleteForm(instance=post)
#     if request.method == "POST":
#         form = GameDeleteForm(request.POST, instance=post)
#         if form.is_valid():
#             post.delete()
#             return redirect('game_details', pk=pk)
#     else:
#         form = GameDeleteForm(instance=post)

#     return render(request, 'game_delete.html',
#                   {
#                       'form': form,
#                       'post': post,
#                   })