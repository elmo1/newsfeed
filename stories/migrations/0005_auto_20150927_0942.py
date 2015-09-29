# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20150927_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='categories',
        ),
        migrations.AddField(
            model_name='story',
            name='categories',
            field=models.ForeignKey(default=0, to='stories.Category'),
            preserve_default=False,
        ),
    ]
