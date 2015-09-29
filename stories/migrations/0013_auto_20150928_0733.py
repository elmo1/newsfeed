# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0012_remove_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='category',
            field=models.ForeignKey(to='stories.Category'),
        ),
    ]
