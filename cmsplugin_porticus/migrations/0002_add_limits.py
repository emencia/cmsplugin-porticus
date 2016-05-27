# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_porticus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumplugin',
            name='limit',
            field=models.PositiveIntegerField(default=15, help_text='Limit of how many ressource will be showed. 0 means not limit (all ressources).', verbose_name='limit'),
        ),
        migrations.AddField(
            model_name='galleryplugin',
            name='limit',
            field=models.PositiveIntegerField(default=15, help_text='Limit of how many album will be showed. 0 means not limit (all albums).', verbose_name='limit'),
        ),
    ]
