import excavator

from settings import *


PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
GRAPPELLI_INSTALLED = True

#INSTALLED_APPS += excavator.env_list('EXTRA_INSTALLED_APPS', required=True)
INSTALLED_APPS += excavator.env_list('EXTRA_INSTALLED_APPS', required=True)


TEMPLATE_CONTEXT_PROCESSORS += (
    "mezzanine.conf.context_processors.settings",
    "mezzanine.pages.context_processors.page",
)
