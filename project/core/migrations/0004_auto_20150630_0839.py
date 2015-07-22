# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150630_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_title',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='meta_description',
            field=models.CharField(max_length=150, blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='meta_title',
            field=models.CharField(max_length=60, blank=True),
        ),
    ]
