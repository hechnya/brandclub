# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0003_remove_cartitem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart_id', models.CharField(max_length=240)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041e\u0431\u044c\u0435\u043a\u0442 \u0437\u0430\u043a\u0430\u0437\u0430',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
    ]
