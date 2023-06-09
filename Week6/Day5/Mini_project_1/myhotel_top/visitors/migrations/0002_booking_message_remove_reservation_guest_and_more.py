# Generated by Django 4.2.1 on 2023-06-18 11:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.CharField(max_length=100)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('guests_num', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='room',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
        migrations.RemoveField(
            model_name='room',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_cost',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_size',
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Single'), (2, 'Double'), (3, 'Triple'), (4, 'Quad')], default=1),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='RoomSize',
        ),
        migrations.DeleteModel(
            name='RoomType',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='visitors.room'),
        ),
    ]
