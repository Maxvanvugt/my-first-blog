# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-07 09:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160706_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2016, 7, 7, 9, 11, 17, 795788, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
