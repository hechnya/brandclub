# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150723_0804'),
        ('cart', '0009_order_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='parametr',
            field=models.ForeignKey(default=1, to='core.ProductParametr'),
            preserve_default=False,
        ),
    ]
