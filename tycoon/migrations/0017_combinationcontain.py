# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-25 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tycoon', '0016_codetoitem_is_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='CombinationContain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tycoon.Combination')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tycoon.Avatar')),
            ],
        ),
    ]
