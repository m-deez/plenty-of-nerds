# Generated by Django 3.2.9 on 2021-11-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=99)),
                ('system', models.CharField(max_length=100)),
                ('experience_lvl', models.CharField(max_length=100)),
                ('players', models.CharField(max_length=100)),
                ('gm_required', models.BooleanField(default=False)),
                ('game_style', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
