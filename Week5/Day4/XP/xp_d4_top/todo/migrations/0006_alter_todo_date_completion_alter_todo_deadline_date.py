# Generated by Django 4.2.1 on 2023-05-31 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_todo_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_completion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
