# Generated by Django 3.2.9 on 2021-11-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.CharField(default='https://i.imgur.com/cyYLrai.jpg', max_length=250),
        ),
    ]
