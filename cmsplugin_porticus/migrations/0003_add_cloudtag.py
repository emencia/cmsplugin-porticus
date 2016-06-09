# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_porticus', '0002_add_limits'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumplugin',
            name='enable_cloud',
            field=models.BooleanField(default=False, verbose_name='enable cloud tags'),
        ),
    ]
