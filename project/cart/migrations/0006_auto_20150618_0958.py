# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='price',
            field=models.IntegerField(),
        ),
    ]
