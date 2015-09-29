# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_story_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='category',
            field=models.ForeignKey(related_name='categories', to='stories.Category'),
        ),
    ]
