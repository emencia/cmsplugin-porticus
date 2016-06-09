"""
Models of Porticus' DjangoCMS plugins
"""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from porticus.models import Gallery, Album

class GalleryPlugin(CMSPlugin):
    """Plugin config to display a Gallery"""
    gallery = models.ForeignKey(Gallery, verbose_name=_('gallery'),
                                help_text=_('Gallery to display'))

    limit = models.PositiveIntegerField(_('limit'),
                                        default=15,
                                        help_text=_('Limit of how many album will be showed. 0 means not limit (all albums).'))

    template_name = models.CharField(_('template'),
                                     max_length=100,
                                     help_text=_("Template used to render the Gallery's plugin"),
                                     choices=settings.PORTICUS_GALLERY_PLUGIN_TEMPLATE_CHOICES,
                                     default=settings.PORTICUS_GALLERY_PLUGIN_TEMPLATE_DEFAULT,
                                     blank=False)

    def __unicode__(self):
        return self.gallery.name

class AlbumPlugin(CMSPlugin):
    """Plugin config to embed an Album"""
    album = models.ForeignKey(Album, verbose_name=_('album'),
                              help_text=_('Album to display'))

    limit = models.PositiveIntegerField(_('limit'), default=15,
                                        help_text=_('Limit of how many ressource will be showed. 0 means not limit (all ressources).'))

    template_name = models.CharField(_('template'), max_length=100,
                                     help_text=_("Template used to render the Album's plugin"),
                                     choices=settings.PORTICUS_ALBUM_PLUGIN_TEMPLATE_CHOICES,
                                     default=settings.PORTICUS_ALBUM_PLUGIN_TEMPLATE_DEFAULT,
                                     blank=False)

    enable_cloud = models.BooleanField(_('enable cloud tags'), default=False)

    def __unicode__(self):
        return self.album.name
