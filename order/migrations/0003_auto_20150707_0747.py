# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20150707_0743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='m_id',
            new_name='manager',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='w_id',
            new_name='waiter',
        ),
    ]
