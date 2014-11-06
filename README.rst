.. _DjangoCMS: https://www.django-cms.org
.. _South: http://south.readthedocs.org/en/latest/
.. _Porticus: https://github.com/emencia/porticus

cmsplugin_porticus
==================

This is the `DjangoCMS`_ plugins for `Porticus`_ to embed *Album* or *Galleries* in a cms page.

Requires
********

* `DjangoCMS`_ >= 3.x;
* `Porticus`_ >= 0.9.x (for *Porticus < 0.9* and so for *DjangoCMS 2.x* use the plugin version *<0.2* from the branch *djangocms_2*);

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

See the plugin ``settings.py`` file to see what setting you can override.

Note
****

If you previously used the shipped plugin from Porticus, just disable it and enable this one in ``settings.INSTALLED_APPS``, you won't need to syncdb and your page plugins won't be lost. But to fix an issue on Gallery plugin, you will need to pass the South migration '0001' in fake (with ``--fake`` argument) then normally launch the next migrations.