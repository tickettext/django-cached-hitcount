# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cached_hitcount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hit',
            name='added',
            field=models.DateField(default=datetime.datetime.utcnow().date(), db_index=True),
        ),
    ]
