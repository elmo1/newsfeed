# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0014_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='comments',
            field=models.ForeignKey(default=[], to='stories.Comment'),
            preserve_default=False,
        ),
    ]
