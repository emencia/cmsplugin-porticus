"""
Porticus' DjangoCMS plugins
"""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator

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

        # Get the published Gallery albums with optionnal limit (and
        # pagination) if any
        album_list = queryset = Album.published.filter(gallery=instance.gallery)
        pagination = current_page = None
        if instance.limit:
            pagination = Paginator(album_list, instance.limit)
            current_page = pagination.page(1) # Is allways the first page
            album_list = current_page.object_list

        context.update({
            'instance': instance,
            'gallery_instance': instance.gallery,
            'album_list': album_list,
            'pagination': pagination,
            'current_album_page': current_page,
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
        ressource_list = queryset = Ressource.published.filter(album=instance.album)
        pagination = current_page = None
        if instance.limit:
            pagination = Paginator(ressource_list, instance.limit)
            current_page = pagination.page(1) # Is allways the first page
            ressource_list = current_page.object_list

        context.update({
            'instance': instance,
            'album_instance': instance.album,
            'gallery_instance': instance.album.gallery,
            'ressource_list': ressource_list,
            'pagination': pagination,
            'current_ressources_page': current_page,
        })
        return context


plugin_pool.register_plugin(GalleryPlugin)
plugin_pool.register_plugin(AlbumPlugin)
