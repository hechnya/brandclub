# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_characteristics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='characteristics',
            new_name='characters',
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(max_length=65, blank=True),
        ),
    ]
