# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordersys', '0002_auto_20150708_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
