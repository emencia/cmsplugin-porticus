"""
Settings for Porticus' DjangoCMS plugins
"""
PORTICUS_GALLERY_PLUGIN_TEMPLATE_CHOICES = (
    ('porticus/cms/gallery_detail.html', 'Default template'),
)
PORTICUS_ALBUM_PLUGIN_TEMPLATE_CHOICES = (
    ('porticus/cms/album_detail.html', 'Default template'),
)

# Default template choices
PORTICUS_GALLERY_PLUGIN_TEMPLATE_DEFAULT = PORTICUS_GALLERY_PLUGIN_TEMPLATE_CHOICES[0][0]
PORTICUS_ALBUM_PLUGIN_TEMPLATE_DEFAULT = PORTICUS_ALBUM_PLUGIN_TEMPLATE_CHOICES[0][0]
