from django.contrib import admin
from .models import Nerd, System, XPL, GameStyle, Game

# Register your models here.

admin.site.register(Nerd)
admin.site.register(System)
admin.site.register(XPL)
admin.site.register(GameStyle)
admin.site.register(Game)