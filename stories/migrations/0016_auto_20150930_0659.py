# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0015_story_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='moderator',
        ),
        migrations.RemoveField(
            model_name='story',
            name='comments',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
