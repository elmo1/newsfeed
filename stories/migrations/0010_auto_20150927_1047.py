# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_auto_20150927_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='stories',
        ),
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.ForeignKey(related_name='categories', default=0, to='stories.Category'),
            preserve_default=False,
        ),
    ]
