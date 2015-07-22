# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_slide'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': '\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u043e\u0442\u043e \u0432 \u0441\u043b\u0430\u0439\u0434\u0435\u0440', 'verbose_name_plural': '\u0424\u043e\u0442\u043e \u0441\u043b\u0430\u0439\u0434 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b'},
        ),
        migrations.AddField(
            model_name='product',
            name='article',
            field=models.OneToOneField(null=True, blank=True, to='core.Article'),
        ),
    ]
