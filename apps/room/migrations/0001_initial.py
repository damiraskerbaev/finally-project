# Generated by Django 4.2.8 on 2024-03-26 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Number of the room')),
                ('capacity', models.PositiveIntegerField(verbose_name='Capacity of the room')),
                ('price_per_night', models.PositiveBigIntegerField(verbose_name='Price per night')),
                ('is_used', models.BooleanField(verbose_name='Is used')),
                ('description', models.TextField(blank=True, verbose_name='Description of the room')),
                ('image', models.ImageField(upload_to='rooms-image/%Y/%m/%d', verbose_name='Image of the room')),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel', verbose_name='Hotel')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
    ]
