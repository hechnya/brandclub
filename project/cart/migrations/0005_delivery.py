# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=50)),
                ('order', models.OneToOneField(to='cart.Order')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u0430',
            },
        ),
    ]
