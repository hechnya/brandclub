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
                ('meta_title', models.CharField(max_length=60, blank=True)),
                ('meta_description', models.CharField(max_length=150, blank=True)),
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
                ('meta_title', models.CharField(max_length=60, blank=True)),
                ('meta_description', models.CharField(max_length=150, blank=True)),
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
                ('meta_title', models.CharField(max_length=60, blank=True)),
                ('meta_description', models.CharField(max_length=150, blank=True)),
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
                ('video', models.CharField(max_length=200, null=True, blank=True)),
                ('meta_title', models.CharField(max_length=65, blank=True)),
                ('meta_description', models.CharField(max_length=150, blank=True)),
                ('article', models.OneToOneField(null=True, blank=True, to='core.Article')),
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
                ('is_main', models.BooleanField(default=False, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440')),
                ('product', models.ForeignKey(to='core.Product')),
            ],
            options={
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='ProductParametr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField()),
                ('price', models.IntegerField()),
                ('is_main', models.BooleanField(default=False, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440')),
                ('product', models.ForeignKey(to='core.Product')),
            ],
            options={
                'verbose_name': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430',
                'verbose_name_plural': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'slides')),
            ],
            options={
                'verbose_name': '\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u043e\u0442\u043e \u0432 \u0441\u043b\u0430\u0439\u0434\u0435\u0440',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e \u0441\u043b\u0430\u0439\u0434 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
    ]
