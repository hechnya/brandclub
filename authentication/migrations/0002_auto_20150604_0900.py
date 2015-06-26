# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='zip',
            field=models.CharField(max_length=6, blank=True),
        ),
    ]
