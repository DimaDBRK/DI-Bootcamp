# Generated by Django 4.2.1 on 2023-06-02 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_alter_rental_rental_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='name',
        ),
    ]
