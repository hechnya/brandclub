# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150718_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
