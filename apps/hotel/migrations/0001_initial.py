# Generated by Django 4.2.8 on 2024-03-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Hotel of the name')),
                ('address', models.CharField(max_length=512, verbose_name='Address of the hotel')),
                ('city', models.CharField(max_length=64, verbose_name='City')),
                ('country', models.CharField(max_length=64, verbose_name='Country')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=7, verbose_name='Rating of the hotel')),
                ('image', models.ImageField(upload_to='hotels/%Y/%m/%d', verbose_name='Image of the Hotel')),
                ('description', models.TextField(verbose_name='Descrtiption of the Hotel')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
            },
        ),
    ]
