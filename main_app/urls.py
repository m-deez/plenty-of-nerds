from django.urls import path
from . import views, forms


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('nerds/', views.NerdList.as_view(), name='nerd_list'),
    path('nerds/create', views.NerdCreate.as_view(), name='nerd_create'),
    path('nerds/<int:pk>', views.NerdDetails.as_view(), name='nerd_details'),
    path('profile/<int:pk>', views.UserDetails.as_view(), name='user_nerd_details'),
    path('nerds/<int:pk>/update', views.NerdUpdate.as_view(), name='nerd_update'),
    path('nerds/<int:pk>/delete', views.NerdDelete.as_view(), name='nerd_delete'),
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>', views.GameDetails.as_view(), name='game_details'),
    path('games/create', views.game_create, name='game_create'),
    path('games/<int:pk>/edit', views.game_edit, name='game_edit'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='game_delete'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]