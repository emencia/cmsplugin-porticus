"""
Porticus' DjangoCMS plugins
"""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from porticus.models import Album, Ressource

from cmsplugin_porticus.models import GalleryPlugin as GalleryPluginModel
from cmsplugin_porticus.models import AlbumPlugin as AlbumPluginModel

class PorticusPluginBase(CMSPluginBase):
    module = 'Porticus'

class GalleryPlugin(PorticusPluginBase):
    """
    Standard plugin to embed a slideshow
    """
    model = GalleryPluginModel
    name = _('Gallery')
    fields = ('gallery', 'limit', 'template_name')
    render_template = settings.PORTICUS_GALLERY_PLUGIN_TEMPLATE_DEFAULT

    def render(self, context, instance, placeholder):
        self.render_template = instance.template_name

        # Get the publish Gallery albums with optionnal limit if any
        album_list = Album.published.filter(gallery=instance.gallery)
        if instance.limit:
            album_list = album_list[0:instance.limit]

        context.update({
            'instance': instance,
            'gallery_instance': instance.gallery,
            'album_list': album_list,
        })
        return context

class AlbumPlugin(PorticusPluginBase):
    """
    Standard plugin to embed a slideshow
    """
    model = AlbumPluginModel
    name = _('Album')
    fields = ('album', 'limit', 'template_name')
    render_template = settings.PORTICUS_ALBUM_PLUGIN_TEMPLATE_DEFAULT

    def render(self, context, instance, placeholder):
        self.render_template = instance.template_name

        # Get the publish Gallery albums with optionnal limit if any
        ressource_list = Ressource.published.filter(album=instance.album)
        if instance.limit:
            ressource_list = ressource_list[0:instance.limit]

        context.update({
            'instance': instance,
            'album_instance': instance.album,
            'gallery_instance': instance.album.gallery,
            'ressource_list': ressource_list,
        })
        return context

plugin_pool.register_plugin(GalleryPlugin)
plugin_pool.register_plugin(AlbumPlugin)
