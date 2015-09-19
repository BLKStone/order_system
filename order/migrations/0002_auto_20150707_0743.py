# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='order_tea',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='order_tea',
            old_name='tea_id',
            new_name='tea',
        ),
    ]
