# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_productweight_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.AlterField(
            model_name='productweight',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440'),
        ),
    ]
