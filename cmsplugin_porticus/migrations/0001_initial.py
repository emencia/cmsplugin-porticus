# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('porticus', '0001_initial'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template_name', models.CharField(default=b'porticus/cms/album_detail.html', help_text="Template used to render the Album's plugin", max_length=100, verbose_name='template', choices=[(b'porticus/cms/album_detail.html', b'Default template')])),
                ('album', models.ForeignKey(verbose_name='album', to='porticus.Album', help_text='Album to display')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GalleryPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template_name', models.CharField(default=b'porticus/cms/gallery_detail.html', help_text="Template used to render the Gallery's plugin", max_length=100, verbose_name='template', choices=[(b'porticus/cms/gallery_detail.html', b'Default template')])),
                ('gallery', models.ForeignKey(verbose_name='gallery', to='porticus.Gallery', help_text='Gallery to display')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
