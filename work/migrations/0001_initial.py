# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-20 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pieces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='./samples/%Y/')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('publish', models.BooleanField()),
            ],
            options={
                'ordering': ['title'],
                'get_latest_by': 'date',
                'verbose_name_plural': 'Pieces',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='./client-logos/')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('content', models.TextField()),
                ('url', models.URLField(blank=True)),
                ('meta', models.CharField(max_length=900)),
                ('weight', models.PositiveIntegerField(blank=True)),
                ('personal', models.BooleanField()),
                ('publish', models.BooleanField()),
            ],
            options={
                'ordering': ['weight'],
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('content', models.TextField(blank=True)),
                ('icon', models.ImageField(blank=True, upload_to='./services/icons/')),
            ],
            options={
                'ordering': ['title'],
                'get_latest_by': 'date',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('icon', models.ImageField(blank=True, upload_to='./services/tools/')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Tools',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='services',
            field=models.ManyToManyField(blank=True, to='work.Services'),
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.ManyToManyField(blank=True, to='work.Tools'),
        ),
        migrations.AddField(
            model_name='pieces',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Project'),
        ),
    ]