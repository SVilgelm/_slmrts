from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from slmrts.urls import *  # @UnusedWildImport
import os


mediaurls = patterns(
    '',
    (r'^%s(?P<path>.*)$' % 'uploads/', 'django.views.static.serve',
        {'document_root': os.path.join(settings.MEDIA_ROOT, '../uploads/')}),
    (r'^(?P<path>favicon.ico|robots.txt)$', 'django.views.static.serve',
        {'document_root': os.path.join(settings.MEDIA_ROOT, '..')}),
)

urlpatterns = mediaurls + staticfiles_urlpatterns() + urlpatterns
