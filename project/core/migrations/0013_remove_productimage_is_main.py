# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_productimage_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='is_main',
        ),
    ]
