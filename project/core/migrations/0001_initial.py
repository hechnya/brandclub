# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u044c\u0438',
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.ImageField(upload_to=b'article')),
                ('article', models.ForeignKey(to='core.Article')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e \u0441\u0442\u0430\u0442\u044c\u0438',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e \u0441\u0442\u0430\u0442\u044c\u0438',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='core.Category', null=True)),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=150)),
                ('name', models.CharField(max_length=2000)),
                ('page', models.TextField()),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.CreateModel(
            name='PageImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.ImageField(upload_to=b'page')),
                ('page', models.ForeignKey(to='core.Page')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True, max_length=150)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.ManyToManyField(to='core.Category')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b',
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'product')),
                ('product', models.ForeignKey(to='core.Product')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432',
            },
        ),
    ]
