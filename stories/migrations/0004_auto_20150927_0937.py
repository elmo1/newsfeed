# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20150927_0134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='story',
            name='category',
        ),
        migrations.AddField(
            model_name='story',
            name='categories',
            field=models.ManyToManyField(to='stories.Category'),
        ),
    ]
