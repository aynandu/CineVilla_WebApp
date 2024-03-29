# Generated by Django 5.0.1 on 2024-01-30 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('first_Name', models.CharField(max_length=20, unique=True)),
                ('last_Name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('poster', models.ImageField(blank=True, upload_to='moviedetails')),
                ('description', models.CharField(max_length=250)),
                ('release_date', models.DateField()),
                ('actors', models.CharField(max_length=250)),
                ('trailer_Link', models.CharField(blank=True, max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine_app.category')),
            ],
        ),
    ]
