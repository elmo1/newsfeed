# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20150927_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='categories',
        ),
    ]
