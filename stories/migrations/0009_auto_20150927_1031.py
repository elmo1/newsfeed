# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_auto_20150927_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='stories',
            field=models.ManyToManyField(to='stories.Story'),
        ),
    ]
