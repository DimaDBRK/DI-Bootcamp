# Generated by Django 4.2.1 on 2023-05-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='name',
            field=models.CharField(default='animal', max_length=20),
        ),
    ]