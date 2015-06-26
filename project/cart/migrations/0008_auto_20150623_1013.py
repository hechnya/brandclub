# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20150620_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='order',
        ),
        migrations.AddField(
            model_name='delivery',
            name='cart_id',
            field=models.CharField(default='', max_length=240),
            preserve_default=False,
        ),
    ]
