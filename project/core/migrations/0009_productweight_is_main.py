# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_productweight'),
    ]

    operations = [
        migrations.AddField(
            model_name='productweight',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
