from settings import *  # @UnusedWildImport


ADMINS = ()
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'slmrts.localurls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_DIR, 'slmrts.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}
