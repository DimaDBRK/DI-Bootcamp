# Generated by Django 4.2.1 on 2023-05-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0002_alter_category_gifs'),
    ]

    operations = [
        migrations.AddField(
            model_name='gif',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
