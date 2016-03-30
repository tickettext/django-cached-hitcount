# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistIP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(unique=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('added', models.DateField(default=datetime.date(2016, 3, 30), db_index=True)),
                ('object_pk', models.PositiveIntegerField(verbose_name=b'object ID', db_index=True)),
                ('content_type', models.ForeignKey(related_name='content_type_set_for_hit', verbose_name=b'content type', to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-hits',),
                'get_latest_by': 'added',
            },
        ),
    ]
