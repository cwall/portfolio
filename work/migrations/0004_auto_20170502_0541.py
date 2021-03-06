# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-02 05:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_auto_20170502_0523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pieces',
            options={'get_latest_by': 'updated', 'ordering': ['title'], 'verbose_name_plural': 'Pieces'},
        ),
        migrations.AlterField(
            model_name='pieces',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='work.Project'),
        ),
    ]
