# Generated by Django 4.2.1 on 2023-06-05 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_alter_review_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='films.film'),
        ),
    ]
