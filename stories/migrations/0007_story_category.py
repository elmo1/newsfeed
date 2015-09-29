# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_remove_story_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='category',
            field=models.ForeignKey(default=0, to='stories.Category'),
            preserve_default=False,
        ),
    ]
