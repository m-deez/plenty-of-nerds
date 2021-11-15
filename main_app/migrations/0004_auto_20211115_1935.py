# Generated by Django 3.2.7 on 2021-11-15 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_rename_image_game_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='nerd',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='nerd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='main_app.nerd'),
        ),
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.PositiveIntegerField(),
        ),
    ]
