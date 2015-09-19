# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('emp_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('time', models.DateTimeField(verbose_name=b'date published')),
                ('desk_id', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('state', models.IntegerField()),
                ('employee', models.ForeignKey(to='ordersys.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Tea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('order', models.ForeignKey(to='ordersys.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='order_tea',
            name='tea',
            field=models.ForeignKey(to='ordersys.Tea'),
        ),
    ]
