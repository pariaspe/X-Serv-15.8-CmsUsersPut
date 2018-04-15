# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_users_put', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
