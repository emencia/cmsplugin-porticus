.. _DjangoCMS: https://www.django-cms.org
.. _South: http://south.readthedocs.org/en/latest/
.. _Porticus: https://github.com/emencia/porticus

cmsplugin_porticus
==================

This is the `DjangoCMS`_ plugins for `Porticus`_ to embed *Album* or *Galleries* in a cms page.

Links
*****

* Download his `PyPi package <http://pypi.python.org/pypi/cmsplugin-porticus>`_;
* Clone it on his `Github repository <https://github.com/emencia/cmsplugin-porticus>`_;

Requires
********

* Django >= 1.7;
* `DjangoCMS`_ >= 3.1;
* `Porticus`_ >= 1.0.0 (for *Porticus < 0.9* and so for *DjangoCMS 2.x* use the plugin version *<0.2* from the branch *djangocms_2*);

**Warning:** Since ``0.3.0``, database migration has been switched to Django 1.7 migrations system and `South`_ support has been dropped. The `South`_ migration files are still there but moved to ``south_migrations``, resulting in you need ``south==1.x`` to use them. This is only needed if you need to migrate project datas to the last Porticus version, you don't have to care about this if you just start a new project.

Last release version compatible with Django <= 1.6 + `DjangoCMS`_ 3.0 and `Porticus`_ 0.9 is still available on branch ``django_1-6``.

Optional
---------

* `South`_ migration is supported;

Install
*******

In your ``INSTALLED_APPS`` setting : ::

    INSTALLED_APPS = (
        ...
        'cmsplugin_porticus',
        ...
    )

Then add its settings : ::

    from cmsplugin_porticus.settings import *

See the plugin ``settings.py`` file to see what settings you can override.

Usage
*****

Once installed you can insert porticus Galleries or Albums in your page through the CMS toolbar. Each Porticus content in your pages can use a template from the defined ones in your settings.

For Album cloud tags if enabled, you will need to do some CSS to manage size diff between tags, class name start from tag-size-1 to tag-size-XXX where XXX is equivalent to ``settings.PORTICUS_ALBUM_PLUGIN_CLOUD_STEPS`` value (default is 6). Cloud tag html lives inside ``porticus/cms/album_detail.html``.
