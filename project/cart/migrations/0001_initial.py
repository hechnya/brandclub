# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('cart_id', models.CharField(max_length=240)),
                ('parametr', models.ForeignKey(to='core.ProductParametr')),
                ('product', models.ForeignKey(to='core.Product')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u044a\u0435\u043a\u0442 \u043a\u043e\u0440\u0437\u0438\u043d\u044b',
                'verbose_name_plural': '\u041a\u043e\u0440\u0437\u0438\u043d\u0430',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart_id', models.CharField(max_length=240)),
                ('city', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430',
                'verbose_name_plural': '\u0414\u043e\u0441\u0442\u0430\u0432\u043a\u0430',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart_id', models.CharField(max_length=240)),
                ('is_paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041e\u0431\u044c\u0435\u043a\u0442 \u0437\u0430\u043a\u0430\u0437\u0430',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
    ]
