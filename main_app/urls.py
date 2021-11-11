from django.urls import path
from . import views, forms


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('nerds/', views.NerdList.as_view(), name='nerd_list'),
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/create', views.game_create, name='game_create'),
    path('games/edit/<int:pk>', views.game_edit, name='game_edit'),
    path('games/delete/<int:pk>', views.game_delete, name='game_delete'),
]