# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gamapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default=datetime.datetime(2015, 10, 25, 15, 59, 59, 296777, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
