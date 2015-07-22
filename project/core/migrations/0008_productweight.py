# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_product_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductWeight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField()),
                ('price', models.IntegerField()),
                ('product', models.ForeignKey(to='core.Product')),
            ],
            options={
                'verbose_name': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430',
                'verbose_name_plural': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432',
            },
        ),
    ]
